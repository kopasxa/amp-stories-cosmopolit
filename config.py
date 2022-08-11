keywords_for_search = "Best"
min_count_image_on_page = 5
initial_query_for_search = "https://www.cosmopolitan.com/search/?q=COMFY+CLOTHES"
path_to_save_images = "assets/images"
path_to_save_pages = "assets/pages"
publisher = "kopasxa"
publisher_logo = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/How_to_use_icon.svg/1200px-How_to_use_icon.svg.png"
timeout_page_generate = 0.1
path_root = "var/www/8" # path to domain root
path_to_stories = path_root + "/stories"
my_domain = "http://8.eprosto.online/"

style_for_page = """
<style amp-boilerplate>
    body {
    -webkit-animation: -amp-start 8s steps(1, end) 0s 1 normal both;
    -moz-animation: -amp-start 8s steps(1, end) 0s 1 normal both;
    -ms-animation: -amp-start 8s steps(1, end) 0s 1 normal both;
    animation: -amp-start 8s steps(1, end) 0s 1 normal both
    }

    @-webkit-keyframes -amp-start {
    from {
        visibility: hidden
    }

    to {
        visibility: visible
    }
    }

    @-moz-keyframes -amp-start {
    from {
        visibility: hidden
    }

    to {
        visibility: visible
    }
    }

    @-ms-keyframes -amp-start {
    from {
        visibility: hidden
    }

    to {
        visibility: visible
    }
    }

    @-o-keyframes -amp-start {
    from {
        visibility: hidden
    }

    to {
        visibility: visible
    }
    }

    @keyframes -amp-start {
    from {
        visibility: hidden
    }

    to {
        visibility: visible
    }
    }
</style><noscript>
    <style amp-boilerplate>
    body {
        -webkit-animation: none;
        -moz-animation: none;
        -ms-animation: none;
        animation: none
    }
    </style>
</noscript>
<script async src="https://cdn.ampproject.org/v0.js"></script>
<script async custom-element="amp-story" src="https://cdn.ampproject.org/v0/amp-story-1.0.js"></script>
<script async custom-element="amp-ad" src="https://cdn.ampproject.org/v0/amp-ad-0.1.js"></script>
<link href="https://fonts.googleapis.com/css?family=Oswald:200,300,400" rel="stylesheet">
<style amp-custom>
    amp-story {
    font-family: 'Oswald', sans-serif;
    color: #fff;
    }

    amp-story-page {
    background-color: #000;
    }

    h1 {
    font-weight: bold;
    font-size: 2.2em;
    font-weight: normal;
    line-height: 1.174;
    background-color: black;
    }

    p {
    font-weight: normal;
    font-size: 1.3em;
    line-height: 1.5em;
    color: #fff;
    background-color: black;
    }

    q {
    font-weight: 300;
    font-size: 1.1em;
    }

    amp-story-grid-layer.bottom {
    align-content: end;
    }

    amp-story-grid-layer.bottom h4 {
        font-weight: bold;
        font-size: 1.8em;
        font-weight: normal;
        line-height: 1.174;
        background-color: black;
        padding: 0.5em;
        margin-bottom: 2.2em;
    }

    amp-story-grid-layer.noedge {
    padding: 0px;
    }

    amp-story-grid-layer.center-text {
    align-content: center;
    }

    .wrapper {
    display: grid;
    grid-template-columns: 50% 50%;
    grid-template-rows: 50% 50%;
    }

    .banner-text {
    text-align: center;
    background-color: #000;
    line-height: 2em;
    }
</style>"""