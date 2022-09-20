from django.core.management.base import BaseCommand
import feedparser
from dateutil import parser
from podcast.models import Episode
import re

CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')


def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext

def save_new_episodes(feed):
        podcast_title = feed.channel.title
        podcast_image = feed.channel.image['href']
        
        for item in feed.entries:
            if not Episode.objects.filter(guid=item.guid).exists():
                episode = Episode(
                    title=item.title,
                    description=cleanhtml(item.description),
                    link=item.link,
                    image=podcast_image,
                    podcast_name=podcast_title,
                    published=parser.parse(item.published),
                    audio=item['links'][1]['href'],
                    guid=item.guid
                )
                episode.save()

def fetch_talk_python_to_me_episodes():
    _feed = feedparser.parse('https://talkpython.fm/episodes/rss')
    save_new_episodes(_feed)

def fetch_the_real_python_podcast_episodes():
    _feed = feedparser.parse('https://realpython.com/podcasts/rpp/feed')
    save_new_episodes(_feed)


class Command(BaseCommand):

    def handle(self, *args, **options):
        fetch_talk_python_to_me_episodes()
        fetch_the_real_python_podcast_episodes()
        