import scraper
import filter
import summarizer
import sys
import datetime

def main():
    print("Crawling TechCrunch, ZDNet, and Gartner for news...")
    articles = scraper.fetch_all()
    print(f"Total articles fetched: {len(articles)}")
    
    print("Filtering for Edge AI, Robotics, Smart Manufacturing, and AI trends...")
    keywords = ["edge ai", "robotics", "smart manufacturing", "ai trend", "artificial intelligence", "ai", "machine learning"]
    filtered = filter.filter_articles(articles, keywords)
    print(f"Relevant articles found: {len(filtered)}")
    
    if len(filtered) == 0:
        print("No matching articles found today. Try again later!")
        sys.exit(0)
        
    print("\nGenerating AI summaries and LinkedIn insights from multiple sources...\n")
    summary_html = summarizer.generate_summary(filtered)
    
    print("Summary generation complete!")
    
    # HTML Export Logic
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI News Digest</title>
    <style>
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f4f7f6;
            margin: 0;
            padding: 40px 20px;
        }}
        .container {{
            max-width: 850px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
        }}
        h1 {{
            color: #1a202c;
            margin-top: 0;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 15px;
            font-size: 2.2em;
        }}
        h2 {{
            color: #2d3748;
            margin-top: 40px;
            font-size: 1.5em;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 10px;
        }}
        .date {{
            color: #718096;
            font-size: 0.95em;
            margin-bottom: 30px;
            font-weight: 500;
        }}
        
        .ai-list {{
            list-style: none;
            padding: 0;
            margin: 0;
        }}
        .ai-list li {{
            background: #f8fafc;
            border-left: 5px solid #3182ce;
            border-radius: 6px;
            padding: 24px;
            margin-bottom: 24px;
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        .ai-list li:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 12px -2px rgba(0, 0, 0, 0.1);
        }}
        .ai-title {{
            font-weight: 700;
            font-size: 1.3em;
            color: #2d3748;
            margin-bottom: 8px;
            line-height: 1.3;
        }}
        .ai-source {{
            display: inline-block;
            font-size: 0.75em;
            color: #fff;
            background-color: #4a5568;
            padding: 4px 10px;
            border-radius: 9999px;
            text-transform: uppercase; letter-spacing: 0.5px; font-weight: 600; margin-bottom: 12px;
        }}
        .ai-summary {{
            color: #4a5568;
            font-size: 1.05em;
            line-height: 1.6;
        }}
        
        /* The new LinkedIn Insight box */
        .ai-insight {{
            margin-top: 18px;
            padding: 16px;
            background-color: #f0fdf4;
            border-left: 4px solid #4ade80;
            border-radius: 0 6px 6px 0;
            color: #166534;
            font-size: 1.05em;
        }}
        .ai-insight strong {{
            color: #15803d;
            font-weight: 700;
            display: block;
            margin-bottom: 4px;
        }}
        
        .article-list {{
            list-style: none;
            padding: 0;
        }}
        .article-list li {{
            margin-bottom: 15px;
            padding-bottom: 15px;
            border-bottom: 1px solid #edf2f7;
        }}
        .article-list li:last-child {{
            border-bottom: none;
        }}
        .raw-title {{
            font-weight: 600;
            color: #2d3748;
            text-decoration: none;
            display: block;
            margin-bottom: 6px;
            font-size: 1.05em;
        }}
        .raw-title:hover {{
            color: #3182ce;
        }}
        .raw-source {{
            font-size: 0.8em;
            color: #718096;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Daily AI & Manufacturing News</h1>
        <div class="date">{datetime.datetime.now().strftime('%B %d, %Y')}</div>
        
        <ul class="ai-list">
            {summary_html}
        </ul>
        
        <h2>All Matched Articles</h2>
        <ul class="article-list">
"""
    for a in filtered[:20]:
        html_content += f"""            <li>
                <a href="{a['link']}" class="raw-title" target="_blank">{a['title']}</a>
                <span class="raw-source">{a['source']}</span>
            </li>
"""
    html_content += """        </ul>
    </div>
</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"\\nSuccessfully exported beautiful list-based HTML with LinkedIn insights to index.html!")

if __name__ == "__main__":
    main()
