
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Building LLM Pipelines with Hugging Face & LangChain</h1>

<p>A well-structured repository for learners and early-stage AI practitioners to understand <strong>Hugging Face</strong>, <strong>Transformers</strong>, and <strong>LangChain</strong>, and to learn how to access <strong>open-source</strong> and <strong>closed-source LLMs</strong> efficiently using the <strong>Hugging Face Hub</strong>.</p>

<hr>

<h2>What You Will Learn</h2>
<ul>
<li>Overview of <strong>Hugging Face</strong> and its ecosystem</li>
<li>Difference between <strong>open-source</strong> and <strong>closed-source</strong> LLMs</li>
<li>Basics of the <strong>Transformers library</strong></li>
<li>Using <strong>Hugging Face Pipelines</strong> for inference</li>
<li>Connecting Hugging Face models with <strong>LangChain</strong></li>
<li>How <strong>HuggingFaceHub</strong> and <strong>HuggingFaceEndpoint</strong> work</li>
<li>Common pitfalls and best practices for LLM usage</li>
</ul>

<h2>Target Audience</h2>
<ul>
<li>Beginners exploring <strong>LLMs and Generative AI</strong></li>
<li>Students building AI/ML projects</li>
<li>Learners confused about <strong>Transformers vs LangChain</strong></li>
<li>Anyone seeking a <strong>clear mental model</strong> of LLM access</li>
</ul>

<hr>

<h2>Repository Structure</h2>
<pre>
LangChain-HuggingFace-LLM-Guide/
│
├── notebooks/
│   ├── hf_langchain_llm_access.ipynb
│   └── transformers_pipeline_basics.ipynb
├── README.md
├── requirements.txt
├── .env.example
└── LICENSE
</pre>

<hr>

<h2>Notebook Overview</h2>

<h3>1. hf_langchain_llm_access.ipynb</h3>
<p><strong>Purpose:</strong> Demonstrates how to access open-source and closed-source LLMs hosted on Hugging Face using LangChain.</p>
<p><strong>Key Concepts Covered:</strong></p>
<ul>
<li>Understanding <strong>Hugging Face Hub</strong></li>
<li>Differences between <code>HF_TOKEN</code> and <code>HUGGINGFACEHUB_API_TOKEN</code></li>
<li>Authentication for gated/closed models</li>
<li>How LangChain treats Hugging Face models as <strong>generic LLM interfaces</strong></li>
</ul>

<p><strong>Important Components:</strong></p>
<ul>
<li><code>HuggingFaceHub</code></li>
<li><code>HuggingFaceEndpoint</code></li>
<li>Token-based authentication via <code>.env</code></li>
</ul>

<p><strong>Insight:</strong> Once exposed as an endpoint, LangChain does not differentiate between open-source and closed-source models. Behavior customization is limited in regular LLMs; chat memory is best supported with chat models.</p>

<h3>2. transformers_pipeline_basics.ipynb</h3>
<p><strong>Purpose:</strong> Introduces the Transformers library and shows how to use Hugging Face models independently of LangChain using pipelines.</p>
<p><strong>Key Concepts Covered:</strong></p>
<ul>
<li>The role of <code>pipeline()</code> in model inference</li>
<li>Loading models from Hugging Face Hub</li>
<li>Differences between <code>text-generation</code>, <code>summarization</code>, <code>sentiment-analysis</code>, and other pipelines</li>
<li>How inference works internally</li>
</ul>

<p><strong>Why This Matters:</strong> Understanding Transformers is crucial before using LangChain. Once you grasp the foundation, orchestrating LLMs with LangChain becomes intuitive.</p>

<hr>

<h2>Open-Source vs Closed-Source Models</h2>
<table>
<tr><th>Feature</th><th>Open-Source LLMs</th><th>Closed / Gated LLMs</th></tr>
<tr><td>Model Access</td><td>Public</td><td>Requires token approval</td></tr>
<tr><td>Examples</td><td>GPT-2, Falcon, Mistral</td><td>LLaMA 2, Mixtral Instruct</td></tr>
<tr><td>Cost</td><td>Free</td><td>May have usage limits</td></tr>
<tr><td>Token Required</td><td>Optional</td><td>Mandatory</td></tr>
</table>

<p>Note: Even open-source models require authentication when accessed via Hugging Face Hub APIs.</p>

<hr>

<h2>Environment Variable Setup</h2>
<p>Create a <code>.env</code> file:</p>
<pre>
HUGGINGFACEHUB_API_TOKEN=your_token_here
</pre>
<p>Load securely in Python:</p>
<pre>
from dotenv import load_dotenv
load_dotenv()
</pre>

<hr>

<h2>Common Errors and How to Resolve</h2>
<ul>
<li>Model not found → Check model name and access permissions</li>
<li>401 Unauthorized → Token missing or invalid</li>
<li>LangChain treats model as a regular LLM → Expected behavior; chat features require chat models</li>
</ul>

<hr>

<div class="section">
        <h2>📦 Download & Load Hugging Face Models Locally</h2>
 </div>
        <p>
            This project includes an example showing how to download a Hugging Face
            model once, store it locally, and reload it without repeatedly accessing
            the Hugging Face Hub.
        </p>
 </div>
        <h3>✅ Why Local Model Loading?</h3>
        <ul>
            <li>Faster inference after initial download</li>
            <li>Offline or restricted-network execution</li>
            <li>Better integration with LangChain pipelines</li>
            <li>Reduced dependency on external endpoints</li>
        </ul>
    </div>
 </div>
    <div class="section">
        <h2>📁 Project Structure</h2>
 </div>
        <pre>
Building-LLM-Pipelines-with-Hugging-Face-LangChain/
│
├── models/
│   └── deepseek/
│       └── download_and_load_hf_model.py
│
├── README.md
├── README.html
├── requirements.txt
└── .env
        </pre>
    </div>
 </div>
    <div class="section">
        <h2>🔐 Environment Configuration</h2>
 </div>
        <p>
            Store your Hugging Face access token securely using a <code>.env</code> file.
        </p>
 </div>
        <pre>
hf=your_huggingface_token_here
        </pre>
 </div>
        <p>
            The token is loaded at runtime using <code>python-dotenv</code>, avoiding
            hard-coded secrets in source files.
        </p>
    </div>
 </div>
    <div class="section">
        <h2>📄 Example Script</h2>
 </div>
        <p>
            The following script demonstrates how to:
        </p>
 </div>
        <ul>
            <li>Load Hugging Face credentials</li>
            <li>Download the DeepSeek Coder 1.3B Instruct model</li>
            <li>Save the model and tokenizer locally</li>
            <li>Reload the model from disk</li>
        </ul>
 </div>
        <p>
            File location:
            <code>models/deepseek/download_and_load_hf_model.py</code>
        </p>
    </div>


<h2>Recommended Dependencies</h2>
<pre>
langchain
transformers
huggingface_hub
python-dotenv
torch
</pre>

<hr>

<h2>License</h2>
<p>MIT License — Free to use, learn, and share.</p>

<hr>

<h2>Contribution</h2>
<p>This repository is beginner-focused. If anything is unclear, it indicates an opportunity for improvement. Open issues or submit pull requests to enhance examples, explanations, or notebooks.</p>

<hr>

<h2>Final Note</h2>
<p>If this repository helped you understand LLMs, Hugging Face, or LangChain, consider starring it and sharing with other learners. Happy learning!</p>

</body>
</html>
