Retrieval Augmented Generation (RAG)

# Steps
1. Determine the website URL
2. Parse the sitemap.xml (<website-url>/sitemap.xml) file to get all the sub URLs
3. Extract documents (the text content) from each sub URL [Langchain Document Loader]
4. Split the documents into chunks [Langchain Text Splitter]
5. Create embeddings (vector representations) for each chunk [Langchain Embeddings - OpenAI]
6. Store the embeddings in a vector database [Langchain Vector Store - FAISS] that allows for efficient similarity searches based on the proximity of these vectors
7. Effectively creating a semantic index where similar data points are located close to each other in the embedding space. 

8. USER will ask a question
9. The question is passed to the vector database
10. The vector database returns the RANKED RESULTS (most similar vectors to the question / chunks)
11. Supply the question and the ranked results to an LLM (OpenAI)
12. The LLM will return the answer to the user's question

# Flow
URLs -> Documents -> Chunks -> Embeddings -> Vector Database
Question -> Vector Database -> Ranked Results -> LLM -> Answer

# Tools
- Langchain
- OpenAI
- FAISS

# Deploying app on EC2
1. Update Github variables including EC2_SSH_KEY - Get private key from ~/.ssh/ec2_deploy_key in local
2. Created new Target group for the app
3. Update HTTPS listener of the existing ALB to use the new target group
4. Create new ACM certificate for the domain
5. Add certificate to the ALB
  - From AWS Docs, The certificate selection is handled by SNI, not by the rules. As long as both certificates are added to the listener and the hostnames match, it will work automatically.
6. Update security group of the EC2 to allow inbound traffic from the ALB security group
7. Update the DNS record of the domain to point to the ALB
