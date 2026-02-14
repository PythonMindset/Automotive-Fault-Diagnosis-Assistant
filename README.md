# Automotive Fault Diagnosis Assistant

![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)

**GitHub**: [PythonMindset/Automotive-Fault-Diagnosis-Assistant](https://github.com/PythonMindset/Automotive-Fault-Diagnosis-Assistant)

A hybrid **Generative AI + Retrieval-Augmented Generation (RAG)** system that provides intelligent automotive fault diagnosis. The platform combines semantic search with FAISS embeddings for knowledge retrieval and Google Gemini API for context-aware response generation, demonstrating a modern hybrid architecture for AI-powered expert systems.

## Key Features

### Hybrid Architecture
- **RAG Component**: Semantic search with FAISS embeddings retrieves relevant automotive fault solutions from pre-processed dataset
- **GenAI Component**: Google Gemini 2.5 Flash API generates structured, context-aware diagnostic guidance

### Functionality
- **Intelligent Diagnosis**: Multi-step diagnostic advice based on combined retrieval and generation
- **Semantic Understanding**: Advanced text embeddings with `sentence-transformers` (all-MiniLM-L6-v2) model
- **Query Caching**: Fast responses for repeated queries using JSON-based history
- **User-Friendly Interface**: Clean, responsive web interface with loading animations
- **Structured Output**: Plain-text diagnostic steps with clear recommendations
- **Lightweight & Efficient**: Minimal dependencies, optimized for performance

## Table of Contents

- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Key Components](#key-components)
- [Configuration](#configuration)
- [Usage Examples](#usage-examples)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Project Structure

```
.
├── app.py                          # Flask application entry point
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── data/
│   ├── automotive_faults.csv       # Original automotive fault dataset
│   └── processed_automotive_faults.csv  # Processed dataset with chunks
├── modals/
│   ├── main.py                     # Gemini API integration and response generation
│   ├── bot.py                      # Semantic search using FAISS and embeddings
│   ├── history.py                  # Query caching and response management
│   ├── model.ipynb                 # Jupyter notebook for model training/experimentation
│   ├── chunk_faiss_index.index     # Pre-built FAISS index for semantic search
│   ├── chunk.npy                   # Pre-computed embeddings for dataset chunks
│   └── query_history.json          # Cache of past queries and responses
├── static/
│   ├── script/
│   │   ├── index.js                # Frontend logic for main page
│   │   └── result.js               # Frontend logic for results page
│   └── style/
│       ├── index.css               # Styling for main page
│       └── result.css              # Styling for results page
└── templates/
    ├── index.html                  # Main diagnostic input page
    └── result.html                 # Results display page
```

## How It Works

### 1. **User Input**
User describes their vehicle problem in natural language (e.g., "My engine keeps overheating and the AC stops cooling whenever I'm idling at a signal.")

### 2. **Query Processing**
The system processes the user query through the following pipeline:

1. **Text Normalization**: Converts query to lowercase and removes special characters
2. **Embedding Generation**: Converts the query to a numerical embedding using `all-MiniLM-L6-v2` sentence transformer
3. **Semantic Search**: Uses FAISS to find the 2 most similar entries from the automotive fault database
4. **Cache Check**: Looks up if an identical query has been processed before

### 3. **AI Response Generation**
- Retrieved chunks and user query are sent to Google Gemini API
- Gemini generates structured diagnostic advice following a specific format:
  - Recommendation
  - Step-by-step diagnosis process
  - What to look for and what signs indicate problems
  - Immediate actions users can take

### 4. **Response Caching**
Responses are automatically saved for future reference, improving response time for similar queries.

## Installation

### Prerequisites
- Python 3.8+
- Google Gemini API key

### Setup Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PythonMindset/Automotive-Fault-Diagnosis-Assistant.git
   cd Automotive-Fault-Diagnosis-Assistant
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Key:**
   Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
   
   Get your API key from [Google AI Studio](https://aistudio.google.com)

5. **Run the application:**
   ```bash
   python app.py
   ```

6. **Access the application:**
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Dependencies

- **flask**: Web framework for building the application
- **google-genai**: Official Google Gemini API client
- **pandas**: Data processing and manipulation
- **numpy**: Numerical computations
- **sentence-transformers**: Pre-trained models for generating text embeddings
- **faiss-cpu**: Efficient similarity search and clustering library
- **python-dotenv**: Environment variable management

See `requirements.txt` for specific versions.

## Key Components

### `app.py` - Flask Application
- Main entry point for the web application
- Handles GET/POST requests from the user interface
- Routes requests to the diagnostic backend

### `modals/main.py` - Gemini Integration
- Manages communication with Google Gemini API
- Generates formatted diagnostic responses
- Implements response caching with history module
- Uses temperature=0.25 for consistent, focused responses

### `modals/bot.py` - Semantic Search Engine
- Loads pre-computed FAISS index and embeddings
- Converts user queries to embeddings
- Performs similarity search to find relevant fault descriptions
- Returns top-2 similar entries from the dataset

### `modals/history.py` - Query Caching
- Stores query-response pairs in JSON format
- Implements query normalization for cache matching
- Provides fast retrieval for repeated queries

## Configuration

### Response Format
Responses follow a standardized format for clarity:
- Plain text format (no markdown)
- 1-2 line explanations per step
- Structured diagnosis steps
- Clear recommendations at the beginning
- Empty lines between steps for readability

### Model Parameters
- **Model**: `gemini-2.5-flash` (fast and efficient)
- **Temperature**: 0.25 (low randomness for consistent answers)
- **Max Output Tokens**: 1200 (sufficient for detailed diagnostics)
- **Similarity Search**: Returns top 2 most relevant chunks

## Data

The project includes two CSV datasets:
- `automotive_faults.csv`: Original fault descriptions and solutions
- `processed_automotive_faults.csv`: Processed dataset with chunks and embeddings

The processed dataset has been chunked to optimize semantic search and pre-embedded using the sentence-transformers model.

## Usage Examples

### Example 1: Engine Overheating
```
Input: "My engine keeps overheating and the AC stops cooling whenever I'm idling at a signal."

Output:
Based on your symptoms, it is recommended to have your vehicle serviced immediately.

Diagnosis steps:
1. Check coolant level in the radiator — look for proper coolant level and color (should be green/red depending on type)
2. Inspect the AC compressor clutch — listen for clicking sounds and ensure the AC is engaging properly
...
```

### Example 2: Cached Response
If the user submits the exact same query again, the cached response is returned instantly without API calls.

## Future Enhancements

- Multi-language support
- Database integration for larger fault datasets
- User authentication and diagnostic history
- Mobile application
- Real-time vehicle diagnostics integration
- Enhanced error handling and fallback mechanisms
- Support for multiple Gemini models
- Advanced analytics on common failures

## Troubleshooting

### API Key Issues
- Ensure `.env` file is in the project root directory
- Verify the API key is valid and has appropriate permissions

### FAISS Index Errors
- Ensure `chunk_faiss_index.index` and `chunk.npy` files exist in the `modals/` directory
- Re-run the notebook to rebuild indices if corrupted

### Dataset Not Found
- Verify CSV files exist in the `data/` directory
- Check file paths in `bot.py` for correct relative paths

### Response Timeouts
- Check internet connection for Gemini API access
- Verify API quota limits haven't been exceeded
- Consider increasing `max_output_tokens` parameter

## Development

### Training New Models
The `modals/model.ipynb` Jupyter notebook contains the workflow for:
- Processing raw automotive fault data
- Generating embeddings
- Creating FAISS indices
- Testing the search functionality

Run this notebook to understand the ML pipeline or retrain with new data.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This project was created as part of academic coursework for the PFAI (Project for AI) university initiative, 4th Semester.

## Contributing

This is an academic project. If you'd like to contribute improvements, suggestions, or find issues:
1. Feel free to open an Issue for bugs or feature requests
2. Fork and create a Pull Request for improvements
3. Ensure code follows the existing style and structure

## Citation

If you use this project in your research or coursework, please cite it as:

```bibtex
@software{pfai_automotive_diagnosis_2026,
  author = {PythonMindset},
  title = {Automotive Fault Diagnosis Assistant: A Hybrid GenAI + RAG System},
  year = {2026},
  url = {https://github.com/PythonMindset/Automotive-Fault-Diagnosis-Assistant}
}
```

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the Jupyter notebook in `modals/model.ipynb`
3. Verify all dependencies are correctly installed
4. Ensure the `.env` file is properly configured

---

**Status**: ✅ Active Development  
**Version**: 1.0  
**Last Updated**: February 2026