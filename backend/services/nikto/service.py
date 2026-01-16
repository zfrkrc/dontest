import sys
import os
import json
sys.path.append('/app')
from services.base.tool_service import BaseToolService
import subprocess
from typing import Dict, Any

class NiktoService(BaseToolService):
    def __init__(self):
        super().__init__(service_name='nikto', version='1.0.0')
    
    async def scan(self, target: str, options: Dict[str, Any]) -> Dict[str, Any]:
        # Nikto doesn't have native JSON output, so we'll parse text output
        cmd = ['nikto', '-h', target, '-nointeractive']
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        
        # Parse Nikto output and create findings
        findings = []
        for line in result.stdout.split('\n'):
            line = line.strip()
            # Nikto findings start with "+"
            if line.startswith('+ '):
                findings.append({
                    'msg': line[2:].strip(),  # Remove "+ " prefix
                    'severity': 'Medium'
                })
        
        # Save to JSON file
        output_data = {'vulnerabilities': findings}
        return {
            'findings': findings,
            'raw_output': result.stdout,
            'metadata': {'command': ' '.join(cmd)},
            'output_data': output_data
        }

if __name__ == '__main__':
    NiktoService().run()
