import json
import os

from django.core.management.base import BaseCommand
from Foods.models import Food, SpecialDiet
from urllib import request as request
from urllib.parse import urlparse
import requests
from django.core.files.base import ContentFile
from icrawler.builtin import GoogleImageCrawler
import glob
from django.core.files import File
import urllib.request as urllib2
import simplejson
from io import StringIO


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('food.json', type=str)

    def handle(self, *args, **options):
        with open(options['food.json']) as f:
            data_list = json.load(f)
        dict={}
        # all_images = glob.glob('./downloads/' + '*.*')
        # imageDict = {}
        # for i in all_images:
        #     sp=i.split('/')[2]
        #     imageDict[sp.split('.')[0]] = i
        #     print(sp)
        for j, i in enumerate(['vegan', 'vegetarian', 'wheat/gluten-free', 'dairy free', 'nut', "seafood"]):
            d1= SpecialDiet(diet=i)
            d1.save()
            dict[i]=d1.pk
            print(d1.pk, i)
        for k, data in enumerate(data_list):
            if k < 684:
                print(data)
            # data['pk'] = k
            # Song.objects.get_or_create(pk=data['pk'], defaults=data)
                dietlist = []
                img= data['title']+".jpg"
                food = Food(title=data['title'], rating=data['rating'], calories=data['calories'], fat=data['fat'],
                            sodium=data['sodium'], protein=data['protein'], image=img)
                food.save()
                for i in ['vegan', 'vegetarian', 'wheat/gluten-free', 'dairy free', 'nut', "seafood"]:
                    if data[i] == 1:
                    #obj= SpecialDiet(diet= i).save()
                        food.diet.add(SpecialDiet.objects.get(pk=dict[i]))
            #food.diet.set(dietlist)

                name = data['title']
            # google_crawler = GoogleImageCrawler(storage={'root_dir': './downloads/' + name})
            # google_crawler.crawl(keyword=name, max_num=1)

                #latest = imageDict[name]

            # os.rename(latest, (newname))
            # # path= "./downloads/"+
            #
                #food.image.save(name, File(open(latest, 'rb')), save=True)
                food.save()
