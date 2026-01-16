import sys
sys.path.append('/app')
from services.base.tool_service import BaseToolService
import subprocess
from typing import Dict, Any

class ZapService(BaseToolService):
    def __init__(self):
        super().__init__(service_name='zap', version='1.0.0')
    
    async def scan(self, target: str, options: Dict[str, Any]) -> Dict[str, Any]:
        cmd = ['zap', target]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        return {'findings': [], 'raw_output': result.stdout, 'metadata': {'command': ' '.join(cmd)}}

if __name__ == '__main__':
    ZapService().run()
