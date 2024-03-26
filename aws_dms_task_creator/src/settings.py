def task_settings():
    settings = {
        "Logging": {
            "EnableLogging": True,
            "EnableLogContext": True,
            "LogComponents": [
                {"Severity": "LOGGER_SEVERITY_DEFAULT", "Id": component} for component in [
                    "TRANSFORMATION", "SOURCE_UNLOAD", "IO", "TARGET_LOAD", "PERFORMANCE",
                    "SOURCE_CAPTURE", "SORTER", "REST_SERVER", "VALIDATOR_EXT", "TARGET_APPLY",
                    "TASK_MANAGER", "TABLES_MANAGER", "METADATA_MANAGER", "FILE_FACTORY",
                    "COMMON", "ADDONS", "DATA_STRUCTURE", "COMMUNICATION", "FILE_TRANSFER"
                ]
            ]
        },
        "StreamBufferSettings": {
            "StreamBufferCount": 3,
            "CtrlStreamBufferSizeInMB": 5,
            "StreamBufferSizeInMB": 8
        },
        "ErrorBehavior": {
            "FailOnNoTablesCaptured": True,
            "ApplyErrorUpdatePolicy": "LOG_ERROR",
            "FailOnTransactionConsistencyBreached": False,
            "RecoverableErrorThrottlingMax": 1800,
            "DataErrorEscalationPolicy": "SUSPEND_TABLE",
            "ApplyErrorEscalationCount": 0,
            "RecoverableErrorStopRetryAfterThrottlingMax": True,
            "RecoverableErrorThrottling": True,
            "ApplyErrorFailOnTruncationDdl": False,
            "DataTruncationErrorPolicy": "LOG_ERROR",
            "ApplyErrorInsertPolicy": "LOG_ERROR",
            "EventErrorPolicy": "IGNORE",
            "ApplyErrorEscalationPolicy": "LOG_ERROR",
            "RecoverableErrorCount": -1,
            "DataErrorEscalationCount": 0,
            "TableErrorEscalationPolicy": "STOP_TASK",
            "RecoverableErrorInterval": 5,
            "ApplyErrorDeletePolicy": "IGNORE_RECORD",
            "TableErrorEscalationCount": 0,
            "FullLoadIgnoreConflicts": True,
            "DataErrorPolicy": "LOG_ERROR",
            "TableErrorPolicy": "SUSPEND_TABLE"
        },
        "TTSettings": {
            "TTS3Settings": None,
            "TTRecordSettings": None,
            "EnableTT": False
        },
        "FullLoadSettings": {
            "CommitRate": 10000,
            "StopTaskCachedChangesApplied": False,
            "StopTaskCachedChangesNotApplied": False,
            "MaxFullLoadSubTasks": 8,
            "TransactionConsistencyTimeout": 600,
            "CreatePkAfterFullLoad": False,
            "TargetTablePrepMode": "DROP_AND_CREATE"
        },
        "TargetMetadata": {
            "ParallelApplyBufferSize": 0,
            "ParallelApplyQueuesPerThread": 0,
            "ParallelApplyThreads": 0,
            "TargetSchema": "",
            "InlineLobMaxSize": 0,
            "ParallelLoadQueuesPerThread": 0,
            "SupportLobs": True,
            "LobChunkSize": 0,
            "TaskRecoveryTableEnabled": False,
            "ParallelLoadThreads": 0,
            "LobMaxSize": 32,
            "BatchApplyEnabled": False,
            "FullLobMode": False,
            "LimitedSizeLobMode": True,
            "LoadMaxFileSize": 0,
            "ParallelLoadBufferSize": 0
        },
        "ControlTablesSettings": {
            "historyTimeslotInMinutes": 5,
            "HistoryTimeslotInMinutes": 5,
            "StatusTableEnabled": False,
            "SuspendedTablesTableEnabled": False,
            "HistoryTableEnabled": False,
            "ControlSchema": "",
            "FullLoadExceptionTableEnabled": False
        },
        "ChangeProcessingTuning": {
            "StatementCacheSize": 50,
            "CommitTimeout": 1,
            "BatchApplyPreserveTransaction": True,
            "BatchApplyTimeoutMin": 1,
            "BatchSplitSize": 0,
            "BatchApplyTimeoutMax": 30,
            "MinTransactionSize": 1000,
            "MemoryKeepTime": 60,
            "BatchApplyMemoryLimit": 500,
            "MemoryLimitTotal": 1024
        },
        "ChangeProcessingDdlHandlingPolicy": {
            "HandleSourceTableDropped": True,
            "HandleSourceTableTruncated": True,
            "HandleSourceTableAltered": True
        }
    }
    return settings