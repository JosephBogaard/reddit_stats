# Reddit Statistics

# The Plan
Originally, I planned to work with PRAW as my API. PRAW is extremely intuitive and easy to work with, but it no longer supports pulling posts by date range.
Thus, I had to work with PushShift.

# The Project
In this project, I iteratively pull data using the PushShift API as it has a limit of 100 records per API call.
This has since stopped working due to Denial of Service from PushShift, likely due to the amount of requests made.
The data of this project are submissions from https://www.reddit.com/r/pics/ for the month of December 2020. There are approximately 37,000 submissions.

# Current Work
Since then, I have been coding to use proxies for my pull requests to retreive all the data needed. However, if I pull from a less-active subreddit, I am more likely to succeed with these requests (as there will be fewer), but I chose /r/pics and /r/videos specifically for the reason they would be busy, thus carrying more data.

# Future Work
After this, I will apply the MatPlotLib plotting library to create graphs for the given metrics.
Additionally, I am hoping to add top level comments for analysis.
Easily added, for another metric, can also be querying the data for number of posts, or comments (if added) for keywords. This can be done easily at runtime or after with most programming languages or excel itself.
