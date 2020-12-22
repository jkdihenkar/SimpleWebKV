# Tekton

## Basic Concepts

* Task: A series of steps that execute commands (In CircleCI this is called a Job)

* Pipeline: A set of Tasks (In CircleCI this is called a Workflow)

* PipelineResource: Input or Output of a Pipeline (for example a git repo or a tar file)
* TaskRun: Defines the execution of a Task
* PipelineRun: Defines the execution of a Pipeline

For example, if we write a Task and want to test it we can execute it with a TaskRun. The same applies for a Pipeline: To execute a Pipeline we need to create a PipelineRun.

## Basic Configs are defined as - 

Task Test -
```yaml
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: run_tests
spec:
  resources:
    inputs:
      - name: repo
        type: git
  steps:
    - name: install_reqs
        image: python:3.9.0
        workingDir: /workspace/repo/
        command: ["pip"]
        args: [
          "install", 
          "--user", 
          "-r", 
          "requirements.txt"
        ]
    - name: run_tests
      image: python:3.9.0
      workingDir: /workspace/repo/
      command: ["pytest"]
      args: ["--junitxml=test-reports/junit.xml"]
```

Pipeline Resource - 

```yaml
apiVersion: tekton.dev/v1alpha1
kind: PipelineResource
metadata:
  name: jkdihenkar-simplewebkv
spec:
  type: git
  params:
    - name: url
      value: https://github.com/jkdihenkar/SimpleWebKV
    - name: revision
      value: master
```
