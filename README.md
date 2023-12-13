
# End to End Event Driven Etl Automation pipline cdk!

This project solution use an aws step functions state machine to orchestrate a serverless data pipline that process raw data as it arrives in s3 raw-zone bucket. Then notify a lambda function on objectcreated event and then the lambda function trigger the step function state mechaine workflow to run glue crawler job and catalog the data. then run another glue etl job on the data and save to consumption-zone bucket as parquet format. then use athena to query the catalog table and save the result to result folder in the consumption but after all process complete. it then use sns to send email to admin on job success or failure


## Project Architecture


```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```