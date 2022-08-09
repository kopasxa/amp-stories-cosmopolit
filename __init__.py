from assets.parser import Parse
import config

parser = Parse()
acticles = parser.search(config.keywords_for_search)

builder = parser.run_page_builder(acticles)