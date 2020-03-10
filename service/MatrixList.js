const matrices = {
    "OutputFormat": "png",
    "MetricWidget": {
        "width": 600,
        "height": 395,
        "metrics": [
            [
                "AWS/EC2",
                "CPUUtilization",
                "InstanceId",
                "i-1234567890abcdef0",
                {
                    "stat": "Average"
                }
            ],
            [
                "AWS/EC2",
                "CPUUtilization",
                "InstanceId",
                "i-0987654321abcdef0",
                {
                    "stat": "Average"
                }
            ]
        ],
        "period": 300,
        "start": "-P30D",
        "end": "PT0H",
        "stacked": false,
        "yAxis": {
            "left": {
                "min": 0.1,
                "max": 1
            },
            "right": {
                "min": 0
            }
        }
    }
}