import json
import boto3
import base64
from metric_sources import metric_sources
from botocore.exceptions import ClientError
from send_email import send_email

cloudwatch = boto3.client('cloudwatch')


def lambda_handler(event, context):

    daily_report_data = []

    for metric_data in metric_sources:
        metric_data = json.dumps(metric_data)

        image_data = cloudwatch.get_metric_widget_image(MetricWidget=metric_data)

        daily_report_data.append(image_data['MetricWidgetImage'])


    send_email(daily_report_data)



