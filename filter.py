def filter_articles(articles, keywords=None):
    if keywords is None:
        keywords = ["edge ai", "robotics", "smart manufacturing", "ai trend", "artificial intelligence", "machine learning", "ai"]
    
    keywords_lower = [k.lower() for k in keywords]
    filtered_articles = []
    
    for a in articles:
        text_to_search = (a['title'] + " " + a['summary']).lower()
        # Ensure we match standalone "ai" so we don't match "faith" 
        # Actually it's simpler to just do standard string 'in' for most, 
        # but for 'ai' we might want regex boundaries. 
        # We'll stick to simple inclusion for broader reach because 'ai' is usually bounded by spaces or punctuation,
        # but " ai " check is safer.
        matched = False
        for k in keywords_lower:
            if k == "ai":
                if " ai " in text_to_search or text_to_search.startswith("ai ") or text_to_search.endswith(" ai"):
                    matched = True
                    break
            elif k in text_to_search:
                matched = True
                break
                
        if matched:
            filtered_articles.append(a)
    
    return filtered_articles
