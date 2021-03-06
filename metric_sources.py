metric_sources = [
    {
        "view": "timeSeries",
        "stacked": False,
        "metrics": [
            ["AWS/EC2", "CPUUtilization", "InstanceId", "i-04ff4349e69966ade", {"id": "m1"}],
            [{"expression": "ANOMALY_DETECTION_BAND(m1, 2)", "label": "CPUUtilization (expected)", "id": "ad1",
              "color": "#666666"}],
            ["AWS/EC2", "CPUUtilization", "InstanceId", "i-0411bd83f4941bf18", {"id": "m2"}],
            ["...", "i-04d58b2598ae392f5", {"id": "m3"}],
            ["...", "i-0511711cc89fb6777", {"id": "m4"}],
            ["...", "i-08a6afebbe92128b7", {"id": "m5"}],
            ["...", "i-0f749e64cbde373ce", {"id": "m6"}],
            ["...", "i-04904ef8aa5c470a6", {"id": "m7"}],
            ["...", "i-0a262104c24e3bcf4", {"id": "m8"}]
        ],
        "region": "ap-northeast-2",
        "title": "BDP - CPUUtilization"
    },
    {
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "BMT - CPUUtilization",
        "stat": "Average",
        "period": 300,
        "metrics": [
            ["AWS/EC2", "CPUUtilization", "InstanceId", "i-01c7542772d44b9c1"],
            ["...", "i-0b0cc2712f8674001"],
            ["...", "i-036bf672f15f8a9ad"],
            ["...", "i-09f73e5752d301b4a"]
        ]
    },
    {
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "BPN, CID - CPUUtilization",
        "stat": "Average",
        "period": 300,
        "metrics": [
            ["AWS/EC2", "CPUUtilization", "InstanceId", "i-08a7ca8f089d45879"],
            ["...", "i-0a7ca8d081c85741d"],
            ["...", "i-0d7145a52ce181b52"],
            ["...", "i-035ef0655dad506db"],
            ["...", "i-02b8ddfc485b18f41"],
            ["...", "i-09019adda8ebade1b"]
        ]
    },
    {
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "CMS - CPUUtilization",
        "stat": "Average",
        "period": 300,
        "metrics": [
            ["AWS/EC2", "CPUUtilization", "InstanceId", "i-09f6fef9880cf1fed"],
            ["...", "i-001045480acc56c7a"],
            ["...", "i-0cd6409fd8cc7137d"],
            ["...", "i-01a0b03ac0264db59"]
        ]
    },
    {
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "DBOT, INF - CPUUtilization",
        "stat": "Average",
        "period": 300,
        "metrics": [
            ["AWS/EC2", "CPUUtilization", "InstanceId", "i-0db68736f89670099"],
            ["...", "i-02d4120ab38084bec"],
            ["...", "i-0ea25bdc53b16cbfb"],
            ["...", "i-01eac11618c204b98"]
        ]
    },
    {
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "VIP - CPUUtilization",
        "stat": "Average",
        "period": 300,
        "metrics": [
            ["AWS/EC2", "CPUUtilization", "InstanceId", "i-086c1be2a703710ab"],
            ["...", "i-0576709efe274ac7f"],
            ["...", "i-0c2f885cfab34d116"],
            ["...", "i-070929449a19a6ff7"],
            ["...", "i-01ed32557885d8d82"],
            ["...", "i-09104a5f4414c112a"]
        ]
    },
    {
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "VOC, WAF- CPUUtilization",
        "stat": "Average",
        "period": 300,
        "metrics": [
            ["AWS/EC2", "CPUUtilization", "InstanceId", "i-088adb53c127092ec"],
            ["...", "i-0f6e0fe9f078e5a56"],
            ["...", "i-07e7583797f6dc465"],
            ["...", "i-06d3b65fa77ecb452"]
        ]
    },

    ## Memory Utilization
    {
        "view": "timeSeries",
        "stacked": False,
        "metrics": [
            ["System/Linux", "MemoryUtilization", "InstanceId", "i-04ff4349e69966ade"],
            ["...", "i-0411bd83f4941bf18"],
            ["...", "i-04d58b2598ae392f5"],
            ["...", "i-0511711cc89fb6777"],
            ["...", "i-08a6afebbe92128b7"],
            ["...", "i-0f749e64cbde373ce"],
            ["...", "i-04904ef8aa5c470a6"],
            ["...", "i-0a262104c24e3bcf4"]
        ],
        "region": "ap-northeast-2",
        "title": "BDP - Memory Utilization"
    },
    {
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "BPN, CID - Memory Utilization",
        "metrics": [
            ["System/Linux", "MemoryUtilization", "InstanceId", "i-08a7ca8f089d45879"],
            ["...", "i-035ef0655dad506db"],
            ["...", "i-0d7145a52ce181b52"],
            ["...", "i-0a7ca8d081c85741d"],
            ["...", "i-02b8ddfc485b18f41"],
            ["...", "i-09019adda8ebade1b"]
        ]
    },

    {
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "CMS - Memory Utilization",
        "metrics": [
            ["System/Linux", "MemoryUtilization", "InstanceId", "i-09f6fef9880cf1fed"],
            ["...", "i-001045480acc56c7a"],
            ["...", "i-0cd6409fd8cc7137d"],
            ["...", "i-01a0b03ac0264db59"]
        ]
    },

    {
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "DBOT, INF - Memory Utilization",
        "metrics": [
            ["System/Linux", "MemoryUtilization", "InstanceId", "i-0db68736f89670099"],
            ["...", "i-02d4120ab38084bec"],
            ["...", "i-0ea25bdc53b16cbfb"],
            ["...", "i-01eac11618c204b98"]
        ]
    },
    {
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "VIP - Memory Utilization",
        "metrics": [
            ["System/Linux", "MemoryUtilization", "InstanceId", "i-0576709efe274ac7f"],
            ["...", "i-0c2f885cfab34d116"],
            ["...", "i-01ed32557885d8d82"],
            ["...", "i-070929449a19a6ff7"]
        ]
    },

    ## RDS CPU Utilization
    {
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "BDP, CID, CMS - RDS CPU Utilization",
        "stat": "Average",
        "period": 300,
        "metrics": [
            ["AWS/RDS", "CPUUtilization", "DBInstanceIdentifier", "ldps-prd-cms-mysql"],
            ["...", "ldps-prd-cid-mstr-meta-mysql"],
            ["...", "ldps-prd-bdp-mysql"]
        ]
    },

    {
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "DBT, LOG, MDP - RDS CPU Utilization",
        "stat": "Average",
        "period": 300,
        "metrics": [
            ["AWS/RDS", "CPUUtilization", "DBInstanceIdentifier", "ldps-prd-dbt-mysql"],
            ["...", "ldps-prd-log-mysql"],
            ["...", "ldps-prd-mdp-mysql"]
        ]
    },

    {
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "MIS, RTS, TRD  - RDS CPU Utilization",
        "stat": "Average",
        "period": 300,
        "metrics": [
            ["AWS/RDS", "CPUUtilization", "DBInstanceIdentifier", "ldps-prd-mis-mysql"],
            ["...", "ldps-prd-rts-mysql"],
            ["...", "ldps-prd-trd-mysql"]
        ]
    },

    ## RDS WriteIOPS
    {
        "metrics": [
            ["AWS/RDS", "WriteIOPS", "DBInstanceIdentifier", "ldps-prd-bdp-mysql"],
            ["...", "ldps-prd-cms-mysql"],
            ["...", "ldps-prd-cid-mstr-meta-mysql"],
            ["...", "ldps-prd-dbt-mysql"]
        ],
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "BDP, CID, CMS, DBT - RDS Write IOPS",
        "stat": "Average",
        "period": 300
    },
    {
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "LOG, MDP, MIS, RTS, TRD - RDS Write IOPS",
        "stat": "Average",
        "period": 300,
        "metrics": [
            ["AWS/RDS", "WriteIOPS", "DBInstanceIdentifier", "ldps-prd-log-mysql"],
            ["...", "ldps-prd-mdp-mysql"],
            ["...", "ldps-prd-mis-mysql"],
            ["...", "ldps-prd-rts-mysql"],
            ["...", "ldps-prd-trd-mysql"]
        ]
    },

    ## RDS READ IOPS
    {
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "BDP, CID, CMS, DBT - RDS READ IOPS",
        "stat": "Average",
        "period": 300,
        "metrics": [
            ["AWS/RDS", "ReadIOPS", "DBInstanceIdentifier", "ldps-prd-bdp-mysql"],
            ["...", "ldps-prd-cid-mstr-meta-mysql"],
            ["...", "ldps-prd-cms-mysql"],
            ["...", "ldps-prd-dbt-mysql"]
        ]
    },

    {
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "LOG, MDP, MIS, RTS, TRD - RDS READ IOPS",
        "stat": "Average",
        "period": 300,
        "metrics": [
            ["AWS/RDS", "ReadIOPS", "DBInstanceIdentifier", "ldps-prd-log-mysql"],
            ["...", "ldps-prd-mdp-mysql"],
            ["...", "ldps-prd-mis-mysql"],
            ["...", "ldps-prd-rts-mysql"],
            ["...", "ldps-prd-trd-mysql"]
        ]
    },

    ## RDS Write Latency
    {
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "BDP, CID, CMS, DBT - RDS WriteLatency",
        "stat": "Average",
        "period": 300,
        "metrics": [
            ["AWS/RDS", "WriteLatency", "DBInstanceIdentifier", "ldps-prd-bdp-mysql"],
            ["...", "ldps-prd-cid-mstr-meta-mysql"],
            ["...", "ldps-prd-cms-mysql"],
            ["...", "ldps-prd-dbt-mysql"]
        ]
    },
    {
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "LOG, MDP, MIS, RTS, TRD - RDS WriteLatency",
        "stat": "Average",
        "period": 300,
        "metrics": [
            ["AWS/RDS", "WriteLatency", "DBInstanceIdentifier", "ldps-prd-log-mysql"],
            ["...", "ldps-prd-mdp-mysql"],
            ["...", "ldps-prd-mis-mysql"],
            ["...", "ldps-prd-rts-mysql"],
            ["...", "ldps-prd-trd-mysql"]
        ]
    },

    ## RDS Read Latency
    {
        "metrics": [
            ["AWS/RDS", "ReadLatency", "DBInstanceIdentifier", "ldps-prd-bdp-mysql"],
            ["...", "ldps-prd-cid-mstr-meta-mysql"],
            ["...", "ldps-prd-cms-mysql"],
            ["...", "ldps-prd-dbt-mysql"]
        ],
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "BDP, CID, CMS, DBT - RDS ReadLatency",
        "stat": "Average",
        "period": 300
    },

    {
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "LOG, MDP, MIS, RTS, TRD - RDS ReadLatency",
        "stat": "Average",
        "period": 300,
        "metrics": [
            ["AWS/RDS", "ReadLatency", "DBInstanceIdentifier", "ldps-prd-log-mysql"],
            ["...", "ldps-prd-mdp-mysql"],
            ["...", "ldps-prd-mis-mysql"],
            ["...", "ldps-prd-rts-mysql"],
            ["...", "ldps-prd-trd-mysql"]
        ]
    },

    ## RedShift CPU Utilization
    {
        "metrics": [
            ["AWS/Redshift", "CPUUtilization", "NodeID", "Leader", "ClusterIdentifier", "ldps-prd-cid-redshift"],
            ["...", "Compute-0", ".", "."],
            ["...", "Compute-1", ".", "."],
            ["...", "Compute-2", ".", "."]
        ],
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "Leader, 0,1,2,3 - CPU Utilization",
        "stat": "Average",
        "period": 300
    },
    {
        "view": "timeSeries",
        "stacked": False,
        "region": "ap-northeast-2",
        "title": "Compute 4,5,6,7 - CPU Utilization",
        "stat": "Average",
        "period": 300,
        "metrics": [
            ["AWS/Redshift", "CPUUtilization", "NodeID", "Compute-4", "ClusterIdentifier", "ldps-prd-cid-redshift"],
            ["...", "Compute-5", ".", "."],
            ["...", "Compute-6", ".", "."],
            ["...", "Compute-7", ".", "."]
        ]
    }
]
