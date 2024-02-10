**FinAnalyticaAI
Your Trusted Financial Advisor in the Digital Age.!**

Are you tired of drowning in a sea of financial reports, struggling to make sense of complex balance sheets and income statements? Look no further! FinAnalyticaAI is here to revolutionize the way you understand company finances.
With FinAnalyticaAI, you gain access to a powerful AI-driven chatbot that effortlessly deciphers financial reports, providing you with insightful analysis and actionable recommendations. Whether you're an investor seeking promising opportunities, a business owner striving to enhance profitability, or a student eager to deepen your financial knowledge, FinAnalyticaAI is your ultimate companion.

With FinAnalyticaAI, you can unlock the true potential of financial reports with just a few clicks. Empower yourself with unparalleled insights and stay ahead of the curve with Fin-Analytica by your side.
Our chatbot leverages cutting-edge algorithms to scrutinize financial data, pinpointing key strengths and weaknesses within company performance. From detecting red flags to identifying growth opportunities, FinAnalyticaAI equips you with the knowledge to make informed decisions in the ever-evolving world of finance.


**Architecture Design**
Utilising key resources offered by sponsers of this Hackathon: Cohere, Weaviate, Langchain, we designed the application to be flexible from the start, with LLM and Retrieval Augmented Generation at its core.
We further focused the intent of our RAG chatbot to excels in parsing and analyzing financial reports within the financial domain, with a particular emphasis on generating insights tailored for the NYSE. 

Data Ingestion:
Utilize Langchain and Cohere for parsing and preprocessing various financial report formats, including PDFs, Excel files, images, and PPTs.
Vector Database (Weaviate):

Implement Weaviate as the vector database to store preprocessed financial documents, enabling efficient storage and retrieval through keyword, vector, and hybrid search functionalities.
Chatbot Development:
Develop the chatbot interface using Cohere Chat and Langchain to provide conversational AI capabilities and context-aware responses.

Query Processing and Content Retrieval:
Process user queries to identify intent and extract relevant keywords, then utilize Weaviate's search capabilities to retrieve pertinent financial content.

Response Generation:
Employ Cohere Chat and Langchain to generate coherent and relevant responses based on the retrieved financial content, presenting answers in natural language via the chatbot interface.

**FinAnalyticaAI Architectural Diagram**
Finance-Domain LLM AI Retrieval Augmented Generative Chatbot

![image](https://github.com/coherehackfinai/enterprise_ai_hackathon/assets/159524395/4e13d3a0-95b0-4466-9189-db5ec533c54c)


**sample response**

![image](https://github.com/coherehackfinai/enterprise_ai_hackathon/assets/159524395/cf2ded3b-d671-4f34-85b7-c81a2cf2c155)









