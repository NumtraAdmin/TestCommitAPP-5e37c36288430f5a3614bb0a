import traceback
import sys
from operations import TopOperation
from operations import JoinOperation
from operations import AggregationOperation
from operations import FormulaOperation
from operations import FilterOperation
from connectors import DBFSConnector
from connectors import CosmosDBConnector
from datatransformations import TranformationsMainFlow
from automl import tpot_execution
from core import PipelineNotification
import json

try: 
	PipelineNotification.PipelineNotification().started_notification('5e37c36288430f5a3614bb0b','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify')
	TestCommitAPP_DBFS = DBFSConnector.DBFSConnector.fetch([], {}, "5e37c36288430f5a3614bb0b", spark, "{'url': '', 'file_type': 'Delimeted', 'dbfs_token': '', 'dbfs_domain': '', 'delimiter': ',', 'is_header': 'Use Header Line'}")

	PipelineNotification.PipelineNotification().completed_notification('5e37c36288430f5a3614bb0b','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e37c36288430f5a3614bb0b','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify','http://104.40.91.74:3200/logs/getProductLogs')
	sys.exit(1)
try: 
	PipelineNotification.PipelineNotification().started_notification('5e37c36288430f5a3614bb0c','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify')
	TestCommitAPP_AutoFE = TranformationsMainFlow.TramformationMain.run(["5e37c36288430f5a3614bb0b"],{"5e37c36288430f5a3614bb0b": TestCommitAPP_DBFS}, "5e37c36288430f5a3614bb0c", spark,json.dumps( {"FE": []}))

	PipelineNotification.PipelineNotification().completed_notification('5e37c36288430f5a3614bb0c','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e37c36288430f5a3614bb0c','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify','http://104.40.91.74:3200/logs/getProductLogs')
	sys.exit(1)
try: 
	PipelineNotification.PipelineNotification().started_notification('5e37c36288430f5a3614bb0d','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify')
	TestCommitAPP_AutoML = tpot_execution.Tpot_execution.run(["5e37c36288430f5a3614bb0c"],{"5e37c36288430f5a3614bb0c": TestCommitAPP_AutoFE}, "5e37c36288430f5a3614bb0d", spark,json.dumps( {"model_type": "classification", "label": "", "features": [], "percentage": "10", "executionTime": "5", "ProjectName": "Retail Scenarios", "PipelineName": "TestCommitAPP", "userid": "567a95c8ca676c1d07d5e3e7", "runid": "", "url_ResultView": "http://104.40.91.74:3200", "experiment_id": "895518857185768"}))

	PipelineNotification.PipelineNotification().completed_notification('5e37c36288430f5a3614bb0d','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify')
except Exception as ex: 
	PipelineNotification.PipelineNotification().failed_notification(ex,'5e37c36288430f5a3614bb0d','567a95c8ca676c1d07d5e3e7','http://104.40.91.74:3200/pipeline/notify','http://104.40.91.74:3200/logs/getProductLogs')
	sys.exit(1)

