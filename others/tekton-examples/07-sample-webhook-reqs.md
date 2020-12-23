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