# agents/hermes_agent.py
import os
from typing import Dict
from datetime import datetime

def format_alert(signal_info: Dict) -> str:
    ts = datetime.utcnow().isoformat()
    state = signal_info.get('state')
    signal = signal_info.get('signal')
    reason = signal_info.get('reason', 'Markov state detected')
    alert = f\"[{ts}] ALERT: state={state} signal={signal} reason={reason}\"
    return alert

def explain_with_llm(signal_info: Dict) -> str:
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        return f\"Simple explanation: state={signal_info.get('state')}, signal={signal_info.get('signal')}\"
    try:
        from langchain import OpenAI
        prompt = f\"You are Hermes, a concise trading assistant. Explain this signal in one short paragraph: {signal_info}\"
        llm = OpenAI(openai_api_key=api_key, temperature=0.2)
        resp = llm(prompt)
        return resp
    except Exception as e:
        return f\"LLM error: {e}; fallback explanation: state={signal_info.get('state')}\"

def save_alert(alert_text: str, path='logs/alerts.log'):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'a', encoding='utf-8') as f:
        f.write(alert_text + '\\n')

def run_hermes(signal_info: Dict):
    alert = format_alert(signal_info)
    explanation = explain_with_llm(signal_info)
    full = alert + '\\n' + explanation
    print(full)
    save_alert(full)
    return {'alert': alert, 'explanation': explanation}
