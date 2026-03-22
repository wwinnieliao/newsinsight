import os
from google import genai

def generate_summary(articles):
    if not articles:
        return "<li>No relevant articles found for Edge AI, Robotics, Smart Manufacturing, or AI trends.</li>"
        
    api_key = os.environ.get('GEMINI_API_KEY')
    if not api_key:
        return "<li style='color:red;'>Error: GEMINI_API_KEY environment variable not set. Please set it using 'export GEMINI_API_KEY=your_key'.</li>"
        
    client = genai.Client()
    
    prompt = (
        "You are an expert AI news summarizer and social media strategist. Your task is to review the following recent articles "
        "and identify the top 5 to 7 most impactful stories related to edge AI, robotics, "
        "smart manufacturing, and the latest AI trends. Ensure you pick stories from a mix of sources if available.

"
        "Return the output EXACTLY as HTML list items (<li>), with no surrounding <ul> tags and no markdown formatting (like ```html). "
        "For each item, use this exact structure:
"
        "<li>
"
        "  <div class='ai-title'>[Article Title]</div>
"
        "  <div class='ai-source'>[Source Name]</div>
"
        "  <div class='ai-summary'>[A 2-sentence punchy summary of why it matters.]</div>
"
        "  <div class='ai-insight'><strong>💡 LinkedIn Insight:</strong> [A 1-2 sentence inspiring, thought-provoking insight based on this news, ready to be posted on LinkedIn to spark professional discussion.]</div>
"
        "</li>

"
        "Here are the articles:

"
    )
    
    for i, a in enumerate(articles[:30]): 
        prompt += f"Title: {a['title']}
Source: {a['source']}
Summary snippet: {a['summary']}
---
"
        
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        text = response.text.replace('```html', '').replace('```', '').strip()
        return text
    except Exception as e:
        return f"<li style='color:red;'>Error communicating with Gemini API: {e}</li>"
