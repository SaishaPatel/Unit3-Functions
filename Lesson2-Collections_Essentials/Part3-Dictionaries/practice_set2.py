def caclulate_engagement_rate(post):
    engagement = post["likes"] + post["comments"] + post["shares"]
    rate = engagement / post["views"] * 100
    if post["views"] == 0 or not post["views"]:
        return 0
    return round(rate, 2)
    # views = post.get("views", 0)
    # if views == 0:
    #     return 0
    
    # likes = post.get("likes", 0)
    # comments = post.get("comments", 0)
    # shares = post.get("shares", 0)
post = {"views": 1000, "likes": 50, "comments": 10, "shares": 5}
print(caclulate_engagement_rate(post))

