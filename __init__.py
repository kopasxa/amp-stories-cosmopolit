from assets.parser import Parse
import config
import time

for item in config.queries:
    parser = Parse()
    acticles = parser.search(item, config.keywords_for_search)

    builder = parser.run_page_builder(acticles)
    time.sleep(config.timeout_page_generate)