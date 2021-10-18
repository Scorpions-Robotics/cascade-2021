from icrawler.builtin import BingImageCrawler

classes = ["robots", "ball", "Human faces"]
number = 200
for c in classes:
    bing_crawler = BingImageCrawler(
        storage={"root_dir": f'data-sets/n/{c.replace(" ",".")}'}
    )
    bing_crawler.crawl(keyword=c, filters=None, max_num=number, offset=0)
