# Multimodal Agentic Data Expert

## Purpose
A full-stack, agent-powered RAG engine for enterprise data: text, tables, PDFs, images. Modular, self-improving, and easy to extend.

## Features
- Multimodal data retrieval (vector search: text, PDFs, tables, images)
- Table agent for CSV/Excel queries
- Feedback agent for learning and refinement
- Error logging and analytics
- Configurable with OpenAI or local models

## Quick Start
1. Clone repo, install dependencies: `pip install -r requirements.txt`
2. Add your OpenAI API key to `.env`
3. Place sample data in `/data`
4. Run: `python src/main.py`
