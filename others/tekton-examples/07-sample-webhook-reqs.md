# Webhooks

Sample webhook requests can be obtained from your repo's webhook settings page - edit the configured webhook and scroll down to `Recent Deliveries`. 

Some Notes:

* Keep the payload configured to use `application/json` content type. 
* For current version of `tekton-pipelines` the `DNS-1123` names are enforced so ensure that when configuring the repo and the pipeline-runs, you have conpitable names. 

For Dev/Test workflows - one can either copy payload and put it into POSTMAN or make CURL requests for easy and repeatable tests. There is an option to redeliver a specific payload right from the GitHub UI - in case one wants to use that. 

When configuring webhooks for Tekton - the event listener emits a event id. This ID can be used to query logs on Loki. 

ex: 
```
$ curl -XPOST -v ${TEKTON-GITHUB-WEBHOOK-URL}/ -d @${SAMPLE-PAYLOAD-FILENAME} \
    -H "X-GitHub-Hook-Installation-Target-Type: repository" \
    -H "content-type: application/json"
{"eventListener":"github-hooks","namespace":"tekton-pipelines","eventID":"<event-id>"}
```

sample LogQL can be: `{namespace: "tekton-pipelines"} |~ "<event-id>"`.

Status Update Issue:

Error: ``

Useful Links:
- https://github.com/tektoncd/pipeline/blob/8bcfd8bd2f5f3ccef96196bd667800e8230f1022/cmd/pullrequest-init/main.go#L74
    - https://github.com/tektoncd/pipeline/issues/1777

```
curl -H "Authorization: token $GITHUB_TOKEN" -X POST https://api.github.com/repos/jkdihenkar/simplewebkv/statuses/2da55db3c9673e5089f92dd2484893ff46ad0c46
{
  "message": "Validation Failed",
  "errors": [
    {
      "resource": "Status",
      "code": "custom",
      "field": "state",
      "message": "state is not included in the list"
    }
  ],
  "documentation_url": "https://docs.github.com/rest/reference/repos#create-a-commit-status"
}
```

So created manually -

```
curl   -X POST   -H "Accept: application/vnd.github.v3+json"   -H "Authorization: token $GITHUB_TOKEN"   https://api.github.com/repos/jkdihenkar/simplewebkv/statuses/2da55db3c9673e5089f92dd2484893ff46ad0c46   -d '{"state":"pending"}'
```

- https://docs.github.com/en/free-pro-team@latest/rest/reference/repos#statuses

Sample:
```
curl -H "Authorization: token $GITHUB_TOKEN" -X POST https://api.github.com/repos/jkdihenkar/test/statuses/9bcde245572c74329827acdcab88792ebb84d578
```

Trying out the github task from catalog:

`kubectl create secret generic github --from-literal token="${GITHUB_TOKEN}" -n tekton-pipelines`

## Testing out Status Check from Docker Img


```
docker run -i --rm \
        -e GITHUB_ACTION=update_state \
        -e GITHUB_TOKEN=XXX \
        -e GITHUB_OWNER=jkdihenkar \
        -e GITHUB_REF="COMMIT-ID-SHA" \
        -e GITHUB_STATE=success \
        -e GITHUB_REPO=simplewebkv \
        -e GITHUB_CONTEXT="test-ci" \
        -e GITHUB_TARGET_URL="http://argo-server-argo.stage-ore-k8s.grofer.io/workflows" \
        cloudposse/github-status-updater:latest
```
