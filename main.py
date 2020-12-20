import praw
import requests
from praw.models import MoreComments


def print_comments(submission, file):

    submission.comment_sort = 'best'
    submission.comment_limit = 5
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, praw.models.MoreComments):
            continue
        file.write(top_level_comment.body + "\n")
        file.write("---------------------------------------------\n")


reddit = praw.Reddit("bot1")
file_name = "ProgrammerHumor.txt"
file = open(file_name, "w")

for submission in reddit.subreddit('ProgrammerHumor').top("day", limit=10):
    file.write("Title: " + submission.title + "\n")
    file.write("Comments:\n")
    print("Procesing post: " + submission.title)
    url = submission.url
    print_comments(submission, file)
    file.write("\n\n")
    if submission.is_self:
        continue
    file_name = submission.title
    if "." == file_name[-1]:
        file_name += "jpg"
    else:
        file_name += ".jpg"
    r = requests.get(url)
    with open(file_name, "wb") as f:
        f.write(r.content)
