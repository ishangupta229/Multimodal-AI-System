# User Manual: Multimodal Agentic Data Expert

## Overview
This tool seamlessly retrieves and analyzes text, tabular, and image data using AI agents. It learns from feedback and is highly customizable.

## Operation
1. Install requirements: `pip install -r requirements.txt`
2. Set environment (.env) and API key for full functionality 
3. Run `python src/main.py`
4. Review outputs in terminal  
5. Add new data to `/data` as needed

## Features
- Multimodal & multitask retrieval
- Feedback & learning agent
- Error logging and analytics
- Easily extensible with new agents

## Extending/Debugging
- Add agents in `src/agents.py`
- Add evaluators in `src/evaluator.py`
- Configure settings in `src/config.py`
- All logs stored in `logs/agentic.log`
