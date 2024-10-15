import WebCrawler
from HTTPClient import HTTPClient

def test_fetch():
    def get_host(host):
        client = HTTPClient(host)
        response = client.fetch()
        return response

    def get_200():
        print(get_host("https://youtube.com"))

    def get_error_404():
        print(get_host("https://python.org/bruhbrhubrhu"))

    def get_error_unresolved():
        print(get_host("https://python.asnethnea"))

    # Run tests
    get_200()
    get_error_404()
    get_error_unresolved()

def test_webcrawler():
    crawler = WebCrawler.WebCrawlerThreaded("foo", 0, "foo")

    def test_regex():
        def test_link():
            print("\nTesting links...............")
            def basic_strings():
                print("Basic strings....")
                test_string = "https://python.org/\nhey there http://localhost.com/"
                links = crawler.extract_links(test_string)
                print(links)

                test_string = "http://natas.labs.overthewire.org/"
                links = crawler.extract_links(test_string)
                print(links)

            def complex_strings():
                print("\nComplex strings....")
                test_string = "https://app.bruh.hey.inet/etc/hosts/bin/bruh.txt"
                links = crawler.extract_links(test_string)
                print(links)
            
            def negatives():
                print("\nNegatives...")
                test_string = "https..app.hey"
                links = crawler.extract_links(test_string)
                print(links)

            def webpage_string():
                print("\nTesting with webpage html....")
                test_string = '''
<!DOCTYPE html>
<html lang="en-US" data-dir="ltr" style="direction: ltr;"  >
<head>
	<title>Pages with excessive number of links | SEO Forum | Moz</title>
	<meta name="viewport" content="width&#x3D;device-width, initial-scale&#x3D;1.0" />
	<meta name="content-type" content="text/html; charset=UTF-8" />
	<meta name="apple-mobile-web-app-capable" content="yes" />
	<meta name="mobile-web-app-capable" content="yes" />
	<meta property="og:site_name" content="Moz" />
	<meta name="msapplication-badge" content="frequency=30; polling-uri=https://moz.com/community/q/sitemap.xml" />
	<meta name="theme-color" content="#ffffff" />
	<meta name="msapplication-square150x150logo" content="/community/q/assets/uploads/system/site-logo.png" />
	<meta name="title" content="Pages with excessive number of links" />
	<meta name="description" content="Pre 2013 it was bad practice to have in excess of 100 links per page, google technical guideline.  Many SEO tools still use it as a warning bell. However Matt Cutts from google - I recall a few years ago - came out and categorically said it is NOT bad pra..." />
	<meta property="og:title" content="Pages with excessive number of links" />
	<meta property="og:description" content="Pre 2013 it was bad practice to have in excess of 100 links per page, google technical guideline.  Many SEO tools still use it as a warning bell. However Matt Cutts from google - I recall a few years ago - came out and categorically said it is NOT bad pra..." />
	<meta property="og:type" content="article" />
	<meta property="article:published_time" content="2016-02-17T07:10:59.000Z" />
	<meta property="article:modified_time" content="2016-02-17T08:48:15.000Z" />
	<meta property="article:section" content="Intermediate &amp;amp; Advanced SEO" />
	<meta property="og:image" content="https://moz.com/community/q/assets/uploads/profile/77292-profileavatar-1619582671334.png" />
	<meta property="og:image:url" content="https://moz.com/community/q/assets/uploads/profile/77292-profileavatar-1619582671334.png" />
	<meta property="og:image" content="https://moz.com/community/q/assets/uploads/system/og-image.jpg" />
	<meta property="og:image:url" content="https://moz.com/community/q/assets/uploads/system/og-image.jpg" />
	<meta property="og:image:width" content="1200" />
	<meta property="og:image:height" content="630" />
	<meta property="og:url" content="https://moz.com/community/q/topic/58032/pages-with-excessive-number-of-links/3" />
	

	<!-- TODO, ensure these are 1:1
	<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	-->

	<!-- Google Tag Manager -->
	<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
	new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
	j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
	'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
	})(window,document,'script','dataLayer','GTM-M5PX5QV');</script>
	<!-- End Google Tag Manager -->

	<link rel="stylesheet" type="text/css" href="/community/q/assets/client.css?v=4jds23d1a2r" />
	<link rel="icon" type="image/x-icon" href="/community/q/assets/uploads/system/favicon.ico?v&#x3D;4jds23d1a2r" />
	<link rel="manifest" href="/community/q/manifest.webmanifest" crossorigin="use-credentials" />
	<link rel="search" type="application/opensearchdescription+xml" title="Moz" href="/community/q/osd.xml" />
	<link rel="apple-touch-icon" href="/community/q/assets/uploads/system/touchicon-orig.png" />
	<link rel="icon" sizes="36x36" href="/community/q/assets/uploads/system/touchicon-36.png" />
	<link rel="icon" sizes="48x48" href="/community/q/assets/uploads/system/touchicon-48.png" />
	<link rel="icon" sizes="72x72" href="/community/q/assets/uploads/system/touchicon-72.png" />
	<link rel="icon" sizes="96x96" href="/community/q/assets/uploads/system/touchicon-96.png" />
	<link rel="icon" sizes="144x144" href="/community/q/assets/uploads/system/touchicon-144.png" />
	<link rel="icon" sizes="192x192" href="/community/q/assets/uploads/system/touchicon-192.png" />
	<link rel="prefetch" href="/community/q/assets/src/modules/composer.js?v&#x3D;4jds23d1a2r" />
	<link rel="prefetch" href="/community/q/assets/src/modules/composer/uploads.js?v&#x3D;4jds23d1a2r" />
	<link rel="prefetch" href="/community/q/assets/src/modules/composer/drafts.js?v&#x3D;4jds23d1a2r" />
	<link rel="prefetch" href="/community/q/assets/src/modules/composer/tags.js?v&#x3D;4jds23d1a2r" />
	<link rel="prefetch" href="/community/q/assets/src/modules/composer/categoryList.js?v&#x3D;4jds23d1a2r" />
	<link rel="prefetch" href="/community/q/assets/src/modules/composer/resize.js?v&#x3D;4jds23d1a2r" />
	<link rel="prefetch" href="/community/q/assets/src/modules/composer/autocomplete.js?v&#x3D;4jds23d1a2r" />
	<link rel="prefetch" href="/community/q/assets/templates/composer.tpl?v&#x3D;4jds23d1a2r" />
	<link rel="prefetch" href="/community/q/assets/language/en-US/topic.json?v&#x3D;4jds23d1a2r" />
	<link rel="prefetch" href="/community/q/assets/language/en-US/modules.json?v&#x3D;4jds23d1a2r" />
	<link rel="prefetch" href="/community/q/assets/language/en-US/tags.json?v&#x3D;4jds23d1a2r" />
	<link rel="prefetch stylesheet" href="/community/q/assets/plugins/nodebb-plugin-markdown/styles/default.css" />
	<link rel="prefetch" href="/community/q/assets/language/en-US/markdown.json?v&#x3D;4jds23d1a2r" />
	<link rel="stylesheet" href="https://moz.com/community/q/assets/plugins/nodebb-plugin-emoji/emoji/styles.css?v&#x3D;4jds23d1a2r" />
	<link rel="canonical" href="https://moz.com/community/q/topic/58032/pages-with-excessive-number-of-links" />
	<link rel="up" href="https://moz.com/community/q/category/16/intermediate-advanced-seo" />
	

	<!-- TODO, prefer local copy of these fonts -->
	<link rel="preconnect" href="https://fonts.gstatic.com">
	<link href="https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&display=swap" rel="stylesheet">
	<link href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@300;400;700&display=swap" rel="stylesheet">
	<script src="https://cdnjs.cloudflare.com/ajax/libs/handlebars.js/4.7.7/handlebars.min.js" integrity="sha512-RNLkV3d+aLtfcpEyFG8jRbnWHxUqVZozacROI4J2F1sTaDqo1dPQYs01OMi1t1w9Y2FdbSCDSQ2ZVdAC8bzgAg==" crossorigin="anonymous"></script>

	<script>
		window._mtm = {
			config: {
				team: 'customer-success',
				service: 'qa',
				page: 'topic',
				env: 'production',
			}
		}
	</script>
	<script src="https://moz.com/tags.js"></script>
	<script>
		var config = JSON.parse('{"relative_path":"/community/q","upload_url":"/assets/uploads","asset_base_url":"/community/q/assets","assetBaseUrl":"/community/q/assets","siteTitle":"Moz","browserTitle":"SEO Forum | Moz","titleLayout":"&#123;pageTitle&#125; | &#123;browserTitle&#125;","showSiteTitle":true,"maintenanceMode":false,"minimumTitleLength":3,"maximumTitleLength":255,"minimumPostLength":8,"maximumPostLength":32767,"minimumTagsPerTopic":1,"maximumTagsPerTopic":5,"minimumTagLength":2,"maximumTagLength":30,"undoTimeout":10000,"useOutgoingLinksPage":false,"allowGuestHandles":false,"allowTopicsThumbnail":false,"usePagination":true,"disableChat":true,"disableChatMessageEditing":true,"maximumChatMessageLength":1000,"socketioTransports":["polling","websocket"],"socketioOrigins":"https://moz.com:*","websocketAddress":"","maxReconnectionAttempts":5,"reconnectionDelay":1500,"topicsPerPage":50,"postsPerPage":50,"maximumFileSize":2048,"theme:id":"nodebb-theme-moz","theme:src":"","defaultLang":"en-US","userLang":"en-US","loggedIn":false,"uid":0,"cache-buster":"v=4jds23d1a2r","topicPostSort":"newest_to_oldest","categoryTopicSort":"newest_to_oldest","csrf_token":"WLxOjHYp-PiX-vz_lhLtuFhUz-IPnb9xB1CI","searchEnabled":true,"searchDefaultInQuick":"titles","bootswatchSkin":"","enablePostHistory":true,"timeagoCutoff":30,"timeagoCodes":["af","am","ar","az-short","az","be","bg","bs","ca","cs","cy","da","de-short","de","dv","el","en-short","en","es-short","es","et","eu","fa-short","fa","fi","fr-short","fr","gl","he","hr","hu","hy","id","is","it-short","it","ja","jv","ko","ky","lt","lv","mk","nl","no","pl","pt-br-short","pt-br","pt-short","pt","ro","rs","ru","rw","si","sk","sl","sq","sr","sv","th","tr-short","tr","uk","ur","uz","vi","zh-CN","zh-TW"],"cookies":{"enabled":false,"message":"[[global:cookies.message]]","dismiss":"[[global:cookies.accept]]","link":"[[global:cookies.learn_more]]","link_url":"https:&#x2F;&#x2F;www.cookiesandyou.com"},"thumbs":{"size":512},"iconBackgrounds":["#f44336","#e91e63","#9c27b0","#673ab7","#3f51b5","#2196f3","#009688","#1b5e20","#33691e","#827717","#e65100","#ff5722","#795548","#607d8b"],"emailPrompt":0,"useragent":{"isYaBrowser":false,"isAuthoritative":true,"isMobile":false,"isMobileNative":false,"isTablet":false,"isiPad":false,"isiPod":false,"isiPhone":false,"isiPhoneNative":false,"isAndroid":false,"isAndroidNative":false,"isBlackberry":false,"isOpera":false,"isIE":false,"isEdge":false,"isIECompatibilityMode":false,"isSafari":false,"isFirefox":false,"isWebkit":false,"isChrome":true,"isKonqueror":false,"isOmniWeb":false,"isSeaMonkey":false,"isFlock":false,"isAmaya":false,"isPhantomJS":false,"isEpiphany":false,"isDesktop":true,"isWindows":false,"isLinux":false,"isLinux64":false,"isMac":true,"isChromeOS":false,"isBada":false,"isSamsung":false,"isRaspberry":false,"isBot":false,"isCurl":false,"isAndroidTablet":false,"isWinJs":false,"isKindleFire":false,"isSilk":false,"isCaptive":false,"isSmartTV":false,"isUC":false,"isFacebook":false,"isAlamoFire":false,"isElectron":false,"silkAccelerated":false,"browser":"Chrome","version":"129.0.0.0","os":"OS X","platform":"Apple Mac","geoIp":{},"source":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36","isWechat":false},"acpLang":"undefined","topicSearchEnabled":false,"composer-default":{},"markdown":{"highlight":1,"highlightLinesLanguageList":[],"theme":"default.css","defaultHighlightLanguage":""},"emojiCustomFirst":false,"spam-be-gone":{},"question-and-answer":{"defaultCid_10":"off","defaultCid_11":"off","defaultCid_12":"off","defaultCid_13":"off","defaultCid_14":"off","defaultCid_15":"off","defaultCid_16":"off","defaultCid_17":"off","defaultCid_18":"off","defaultCid_19":"off","defaultCid_2":"off","defaultCid_20":"off","defaultCid_21":"off","defaultCid_22":"off","defaultCid_23":"off","defaultCid_24":"off","defaultCid_25":"off","defaultCid_26":"off","defaultCid_27":"off","defaultCid_28":"off","defaultCid_29":"off","defaultCid_3":"off","defaultCid_30":"off","defaultCid_31":"off","defaultCid_32":"off","defaultCid_33":"off","defaultCid_34":"off","defaultCid_35":"off","defaultCid_36":"off","defaultCid_37":"off","defaultCid_38":"off","defaultCid_39":"off","defaultCid_4":"on","defaultCid_40":"off","defaultCid_41":"off","defaultCid_42":"off","defaultCid_43":"off","defaultCid_44":"off","defaultCid_45":"off","defaultCid_46":"on","defaultCid_47":"on","defaultCid_48":"off","defaultCid_49":"on","defaultCid_5":"off","defaultCid_50":"on","defaultCid_51":"off","defaultCid_52":"on","defaultCid_53":"on","defaultCid_54":"on","defaultCid_55":"on","defaultCid_56":"on","defaultCid_57":"off","defaultCid_58":"off","defaultCid_59":"off","defaultCid_6":"off","defaultCid_60":"off","defaultCid_61":"off","defaultCid_62":"off","defaultCid_63":"on","defaultCid_64":"on","defaultCid_65":"on","defaultCid_66":"off","defaultCid_67":"off","defaultCid_68":"off","defaultCid_69":"off","defaultCid_7":"off","defaultCid_70":"off","defaultCid_71":"off","defaultCid_8":"off","defaultCid_9":"off","forceQuestions":"off","toggleLock":"off"}}');
		var app = {
			user: JSON.parse('{"uid":0,"username":"Guest","displayname":"Guest","userslug":"","fullname":"Guest","email":"","icon:text":"?","icon:bgColor":"#aaa","groupTitle":"","groupTitleArray":[],"status":"offline","reputation":0,"email:confirmed":false,"unreadData":{"":{},"new":{},"watched":{},"unreplied":{}},"isAdmin":false,"isGlobalMod":false,"isMod":false,"privileges":{"chat":false,"upload:post:image":false,"upload:post:file":false,"signature":false,"invite":false,"group:create":false,"search:content":true,"search:users":false,"search:tags":false,"view:users":true,"view:tags":true,"view:groups":true,"local:login":false,"ban":false,"mute":false,"view:users:info":false},"timeagoCode":"en","offline":true,"isEmailConfirmSent":false}')
		};
	</script>

	
	
	<style>body{font-size:14px !important}</style>
	

	
</head>

<body class="page-topic page-topic-58032 page-topic-pages-with-excessive-number-of-links page-topic-category-16 page-topic-category-intermediate-amp-advanced-seo parent-category-9 parent-category-16 page-status-200 theme-moz user-guest skin-noskin">
	<!-- Google Tag Manager (noscript) -->
	<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-M5PX5QV"
	height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
	<!-- End Google Tag Manager (noscript) -->
	<nav id="menu" class="slideout-menu hidden">
		<section class="menu-section" data-section="navigation">
	<ul class="menu-section-list"></ul>
</section>


	</nav>
	<nav id="chats-menu" class="slideout-menu hidden">
		
	</nav>

	<main id="panel" class="slideout-panel">
		<div class="moz-theme moz-header-wrapper">
			<link href="https://moz.com/assets/dist/styles/reboot-73eb3873.min.css" rel="stylesheet">
<link href="https://moz.com/assets/dist/styles/components/top-nav-a819411b.min.css" rel="stylesheet">
<link type="text/css" href="https://moz.com/assets/dist/styles/components/snippets-grid-77f24533.min.css" rel="stylesheet">
<script src="https://cdn.ziffstatic.com/jst/zdconsent.js" async></script>
<script>window.zdconsent = window.zdconsent || {'run': [], 'cmd':[], 'analytics':[], 'functional':[], 'social':[] };</script>
<script>var _mgn = _mgn || {};
  _mgn = Object.assign(_mgn, {
    env: "production",
    hosts: {
      moz: "https://moz.com",
      ma: "https://analytics.moz.com",
      rank: "https://analytics.moz.com/pro/research/rankings",
      local: "https://moz.com/local",
      localapp: "https://localapp.moz.com/en/app/moz",
      lma: "https://analytics.moz.com/pro/local-market-analytics",
      academy: "https://academy.moz.com"
    },
    urls: {
      gateway_scripts: "https://moz.com/svc/gateway/dist/app.gateway.js",
      gateway_stylesheets: "https://moz.com/svc/gateway/dist/styles.gateway.css",
      forge: "https://moz.com/svc/forge/api.js"
    },
    fetch_user: true,
  });</script>
      

          <div id="mzr-top-nav" class="mzr-navbar-wrapper">
      <a class="visually-hidden" href="#content" rel="noopener">Skip to content</a>
      <nav class="mzr-container mzr-navbar mzr-navbar-expand-md" role="navigation" aria-label="Main navigation">
        <a class="mzr-home-logo" title="Moz Home" href="https://moz.com/" tabindex='1'>
          
<svg aria-labelledby="moz-logo-title-header" role="img" width="85" height="25">
  <title id="moz-logo-title-header">Moz logo</title>
  <path d="M71 16L82.99 3h-25.1c-.48.018-.866.4-.89.882v2.736C54.697 2.696 49.97 0 44.5 0 38.036 0 32.61 3.76 31 8.863V3h-4.38c-1.043.015-1.957.478-2.62 1.177l-8.498 9.325L7 4.177C6.34 3.477 5.427 3.015 4.383 3H0v19h5.117c.492-.024.863-.42.883-.91V12l9.5 10.5L25 12v9.09c.017.49.415.886.905.91H31v-6.863C32.61 20.24 38.036 24 44.5 24c7.732 0 14-5.373 14-12 0-1.038-.17-2.04-.46-3H69L57 22h25.104c.48-.018.872-.403.896-.884V16H71zm-26.452 1.96c-3.764 0-6.818-2.668-6.818-5.96 0-3.293 3.053-5.96 6.818-5.96 3.768 0 6.822 2.668 6.822 5.96s-3.053 5.96-6.822 5.96z"></path>
</svg>
        </a>
        <a title="Menu toggle" class="mzr-mobile-nav-toggle" href="#" aria-expanded="false" aria-controls="mobile-menu" tabindex="2">
          <svg aria-labelledby="mobile-menu-open" class="mzr-nav-icon mzr-icon-menu" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <title id="mobile-menu-open">Menu open</title>
            <path d="M24 3c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1s.45-1 1-1h22c.55 0 1 .45 1 1zM24 12c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1s.45-1 1-1h22c.55 0 1 .45 1 1zM24 21c0 .55-.45 1-1 1H1c-.55 0-1-.45-1-1s.45-1 1-1h22c.55 0 1 .45 1 1z"></path>
          </svg>
          <svg aria-labelledby="mobile-menu-close" class="mzr-nav-icon mzr-icon-close mzr-icon-disabled" viewBox="0 0 24 24">
            <title id="mobile-menu-close">Menu close</title>
            <path d="M13.41 12L24 22.59 22.59 24 12 13.41 1.41 24 0 22.59 10.59 12 0 1.41 1.41 0 12 10.59 22.59 0 24 1.41z"></path>
          </svg>
        </a>
        <div id="mzr-mobile-menu" class="mzr-nav-mobile mzr-navbar-nav">
                    <form class="mzr-mobile-search" action="/search">
            <input type="text" class="mzr-input-search" name="q" placeholder="Search...">
            <button aria-labelledby="mobile-menu-search">
              <svg class="mzr-icon-search" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 18 18">
                <title id="mobile-menu-search">Search</title>
                <path d="M18 16.94l-5.553-5.554C13.417 10.186 14 8.66 14 7c0-3.86-3.14-7-7-7S0 3.14 0 7s3.14 7 7 7c1.66 0 3.185-.584 4.386-1.553L16.94 18 18 16.94zM7 12.5c-3.032 0-5.5-2.467-5.5-5.5S3.968 1.5 7 1.5s5.5 2.467 5.5 5.5-2.468 5.5-5.5 5.5z"/>
              </svg>
            </button>
          </form>
          <ul class="mzr-nav-mobile-menu js-nav-mobile-menu">
            


      
      <li class="mzr-nav-item mzr-dropdown mzr-listmenu " aria-label="Products">
    <a
              href="#"
            class="mzr-dropdown-toggle-mobile"
      title="Products"
              id="mzr-navbarDropdown-1025208"
        role="button"
        aria-controls="#products"
        aria-expanded="false"
        aria-label="Expand Products"
            tabindex="-1"
    >Products</a>

          <div id="products" class="mzr-dropdown-listmenu" aria-expanded="false">
        <div class="mzr-row">
          <ul class="mzr-col-12">
                          
                                                                        
              <li class="js-pro-only-swap">
                <a class="mzr-dropdown-item"
                   title="Moz Pro"
                                      href="https://moz.com/products/pro"
                                  >Moz Pro</a>
              </li>
                          
                                                                                        
              <li class="hidden js-pro-only">
                <a class="mzr-dropdown-item"
                   title="Moz Pro Home"
                                      data-href="/home"
                                  >Moz Pro Home</a>
              </li>
                          
                                                                        
              <li class="js-local-only-swap">
                <a class="mzr-dropdown-item"
                   title="Moz Local"
                                      href="https://moz.com/products/local"
                                  >Moz Local</a>
              </li>
                          
                                                                                        
              <li class="hidden js-local-only">
                <a class="mzr-dropdown-item"
                   title="Moz Local Home"
                                      data-href="/home"
                                  >Moz Local Home</a>
              </li>
                          
                                          
              <li class="">
                <a class="mzr-dropdown-item"
                   title="STAT"
                                      href="http://moz.com/products/stat"
                                  >STAT</a>
              </li>
                          
                                          
              <li class="">
                <a class="mzr-dropdown-item"
                   title="Moz API"
                                      href="https://moz.com/products/api"
                                  >Moz API</a>
              </li>
                          
                                                                                        
              <li class="hidden js-api-only">
                <a class="mzr-dropdown-item"
                   title="Moz API Home"
                                      data-href="/api/dashboard/usage"
                                  >Moz API Home</a>
              </li>
                          
                                          
              <li class="">
                <a class="mzr-dropdown-item"
                   title="Compare SEO Products"
                                      href="https://moz.com/products"
                                  >Compare SEO Products</a>
              </li>
                          
                                          
              <li class="">
                <a class="mzr-dropdown-item"
                   title="Moz Data"
                                      href="https://moz.com/moz-data"
                                  >Moz Data</a>
              </li>
                      </ul>
        </div>
      </div>
      </li>
      
      <li class="mzr-nav-item mzr-dropdown mzr-listmenu " aria-label="Free SEO Tools">
    <a
              href="#"
            class="mzr-dropdown-toggle-mobile"
      title="Free SEO Tools"
              id="mzr-navbarDropdown-1025211"
        role="button"
        aria-controls="#free-seo-tools"
        aria-expanded="false"
        aria-label="Expand Free SEO Tools"
            tabindex="-1"
    >Free SEO Tools</a>

          <div id="free-seo-tools" class="mzr-dropdown-listmenu" aria-expanded="false">
        <div class="mzr-row">
          <ul class="mzr-col-12">
                          
                                          
              <li class="">
                <a class="mzr-dropdown-item"
                   title="Domain Analysis"
                                      href="https://moz.com/free-metrics-limit"
                                  >Domain Analysis</a>
              </li>
                          
                                          
              <li class="">
                <a class="mzr-dropdown-item"
                   title="Keyword Explorer"
                                      href="https://moz.com/explorer"
                                  >Keyword Explorer</a>
              </li>
                          
                                          
              <li class="">
                <a class="mzr-dropdown-item"
                   title="Link Explorer"
                                      href="https://moz.com/link-explorer"
                                  >Link Explorer</a>
              </li>
                          
                                          
              <li class="">
                <a class="mzr-dropdown-item"
                   title="Competitive Research"
                                      href="/competitive-research"
                                  >Competitive Research</a>
              </li>
                          
                                          
              <li class="">
                <a class="mzr-dropdown-item"
                   title="MozBar"
                                      href="https://moz.com/products/pro/seo-toolbar"
                                  >MozBar</a>
              </li>
                          
                                          
              <li class="">
                <a class="mzr-dropdown-item"
                   title="More Free SEO Tools"
                                      href="https://moz.com/free-seo-tools"
                                  >More Free SEO Tools</a>
              </li>
                      </ul>
        </div>
      </div>
      </li>
      
      <li class="mzr-nav-item mzr-dropdown mzr-listmenu " aria-label="Learn SEO">
    <a
              href="#"
            class="mzr-dropdown-toggle-mobile"
      title="Learn SEO"
              id="mzr-navbarDropdown-1025214"
        role="button"
        aria-controls="#learn-seo"
        aria-expanded="false"
        aria-label="Expand Learn SEO"
            tabindex="-1"
    >Learn SEO</a>

          <div id="learn-seo" class="mzr-dropdown-listmenu" aria-expanded="false">
        <div class="mzr-row">
          <ul class="mzr-col-12">
                          
                                          
              <li class="">
                <a class="mzr-dropdown-item"
                   title="Beginner&#039;s Guide to SEO"
                                      href="https://moz.com/beginners-guide-to-seo"
                                  >Beginner&#039;s Guide to SEO</a>
              </li>
                          
                                          
              <li class="">
                <a class="mzr-dropdown-item"
                   title="SEO Learning Center"
                                      href="https://moz.com/learn/seo"
                                  >SEO Learning Center</a>
              </li>
                          
                                          
              <li class="">
                <a class="mzr-dropdown-item"
                   title="Moz Academy"
                                      href="https://moz.com/training"
                                  >Moz Academy</a>
              </li>
                          
                                          
              <li class="">
                <a class="mzr-dropdown-item"
                   title="SEO Q&amp;A"
                                      href="/community/q"
                                  >SEO Q&amp;A</a>
              </li>
                          
                                          
              <li class="">
                <a class="mzr-dropdown-item"
                   title="Webinars, Whitepapers, &amp; Guides"
                                      href="https://moz.com/learn/seo/resources"
                                  >Webinars, Whitepapers, &amp; Guides</a>
              </li>
                      </ul>
        </div>
      </div>
      </li>
      
      <li class="mzr-nav-item  " aria-label="Blog">
    <a
              href="https://moz.com/blog"
            class=""
      title="Blog"
              aria-label="Blog"
            tabindex="-1"
    >Blog</a>

      </li>
      
      <li class="mzr-nav-item mzr-dropdown mzr-listmenu " aria-label="Why Moz">
    <a
              href="#"
            class="mzr-dropdown-toggle-mobile"
      title="Why Moz"
              id="mzr-navbarDropdown-1025220"
        role="button"
        aria-controls="#why-moz"
        aria-expanded="false"
        aria-label="Expand Why Moz"
            tabindex="-1"
    >Why Moz</a>

          <div id="why-moz" class="mzr-dropdown-listmenu" aria-expanded="false">
        <div class="mzr-row">
          <ul class="mzr-col-12">
                          
                                          
              <li class="">
                <a class="mzr-dropdown-item"
                   title="Agency Solutions"
                                      href="https://moz.com/agency-solutions"
                                  >Agency Solutions</a>
              </li>
                          
                                          
              <li class="">
                <a class="mzr-dropdown-item"
                   title="Enterprise Solutions"
                                      href="https://moz.com/enterprise-solutions"
                                  >Enterprise Solutions</a>
              </li>
                          
                                          
              <li class="">
                <a class="mzr-dropdown-item"
                   title="Small Business Solutions"
                                      href="https://moz.com/smb-solutions"
                                  >Small Business Solutions</a>
              </li>
                          
                                          
              <li class="">
                <a class="mzr-dropdown-item"
                   title="Case Studies"
                                      href="/learn/seo/resources?learnContentType=case-study"
                                  >Case Studies</a>
              </li>
                          
                                          
              <li class="">
                <a class="mzr-dropdown-item"
                   title="The Moz Story"
                                      href="https://moz.com/about"
                                  >The Moz Story</a>
              </li>
                          
                                          
              <li class="">
                <a class="mzr-dropdown-item"
                   title="New Releases"
                                      href="https://moz.com/whats-new"
                                  >New Releases</a>
              </li>
                      </ul>
        </div>
      </div>
      </li>
      
            <li class="mzr-nav-item  js-logged-out-only" aria-label="Log in">
    <a
              href="/login"
            class=""
      title="Log in"
              aria-label="Log in"
            tabindex="-1"
    >Log in</a>

      </li>
      
                <li class="mzr-nav-item  hidden js-logged-in-only" aria-label="Log out">
    <a
              data-href="/logout"
            class=""
      title="Log out"
              aria-label="Log out"
            tabindex="-1"
    >Log out</a>

      </li>
          </ul>
        </div>
        <ul class="mzr-navbar-nav mzr-nav-desktop">
          


        <li class="mzr-nav-item mzr-nav-item-desktop mzr-dropdown mzr-megamenu">
    <a
      tabindex="2"
             class="mzr-dropdown-toggle"
                                      data-menu-order="1"
        href="/products"
              id="mzr-navbarDropdown-1025230"
        role="button"
        aria-haspopup="true"
        aria-expanded="false"
        aria-label="Products"
        data-nav-name="products"
          >Products</a>
                            
            <div class="mzr-dropdown-menu mzr-drawer-links-list "
            aria-label="Products submenu">
                

<ul class="mega-columns js-nav-links">
      
                                                                                  
    <li>
      <a class="stretched-link" href="https://moz.com/products/pro" title="Try Moz Pro free" tabindex="-1"
         data-logged-in-href="{&quot;slug&quot;:&quot;moz-pro&quot;,&quot;url&quot;:&quot;https:\/\/analytics.moz.com\/pro&quot;,&quot;title&quot;:&quot;Moz Pro Dashboard&quot;}"  
        >
        Moz Pro
      </a>
      <p>Your all-in-one suite of SEO essentials.</p>
    </li>
              
    <li>
      <a class="stretched-link" href="https://moz.com/products/local" title="Check my presence" tabindex="-1"
         data-logged-in-href="{&quot;slug&quot;:&quot;moz-local&quot;,&quot;url&quot;:&quot;\/login\/localapp&quot;,&quot;title&quot;:&quot;Moz Local Dashboard&quot;}"  
        >
        Moz Local
      </a>
      <p>Raise your local SEO visibility with complete local SEO management.</p>
    </li>
              
    <li>
      <a class="stretched-link" href="/products/stat" title="Book a demo" tabindex="-1"
         
        >
        STAT
      </a>
      <p>SERP tracking and analytics for enterprise SEO experts.</p>
    </li>
              
    <li>
      <a class="stretched-link" href="https://moz.com/products/api" title="Get connected" tabindex="-1"
         data-logged-in-href="{&quot;slug&quot;:&quot;moz-api&quot;,&quot;url&quot;:&quot;\/api\/dashboard\/usage&quot;,&quot;title&quot;:&quot;Moz API Dashboard&quot;}"  
        >
        Moz API
      </a>
      <p>Power your SEO with our index of over 44 trillion links.</p>
    </li>
              
    <li>
      <a class="stretched-link" href="https://moz.com/products" title="" tabindex="-1"
         
        >
        Compare SEO Products
      </a>
      <p>See which Moz SEO solution best meets your business needs.</p>
    </li>
              
    <li>
      <a class="stretched-link" href="https://moz.com/moz-data" title="" tabindex="-1"
         
        >
        Moz Data
      </a>
      <p>Power your SEO strategy &amp; AI models with custom data solutions.<br /></p>
    </li>
  </ul>

  <div class="mzr-ad-block mzr-links-list-ad-full">
                              <img class="" src="https://moz.com/files/cms/nav/ads/DiscoverPro-TopNav-Pro.svg?dm=1717436666" alt="Discover top competitors’ winning content">
        <div class="mzr-ad-copy">
                    <small class="my-1 ">What&#039;s New</small>
                    <h4 class="">Discover top competitors’ winning content</h4>
                            <a href="/whats-new" title="Discover top competitors’ winning content" class="btn btn-yellow btn-sm btn-outline">
          Learn More
                  </a>
          </div>
  </div>
      
      </div>
      </li>
        <li class="mzr-nav-item mzr-nav-item-desktop mzr-dropdown mzr-megamenu">
    <a
      tabindex="3"
             class="mzr-dropdown-toggle"
                                      data-menu-order="2"
        href="/free-seo-tools"
              id="mzr-navbarDropdown-1025233"
        role="button"
        aria-haspopup="true"
        aria-expanded="false"
        aria-label="Free SEO Tools"
        data-nav-name="free-seo-tools"
          >Free SEO Tools</a>
                            
            <div class="mzr-dropdown-menu mzr-drawer-links-list "
            aria-label="Free SEO Tools submenu">
                

<ul class="mega-columns js-nav-links">
      
                          
    <li>
      <a class="stretched-link" href="/domain-analysis" title="" tabindex="-1"
         
        >
        Domain Analysis
      </a>
      <p>Get top competitive SEO metrics like DA, top pages and more.</p>
    </li>
              
    <li>
      <a class="stretched-link" href="https://moz.com/explorer" title="" tabindex="-1"
         
        >
        Keyword Explorer
      </a>
      <p>Find traffic-driving keywords with our 1.25 billion+ keyword index.</p>
    </li>
              
    <li>
      <a class="stretched-link" href="https://moz.com/link-explorer" title="" tabindex="-1"
         
        >
        Link Explorer
      </a>
      <p>Explore over 40 trillion links for powerful backlink data.</p>
    </li>
              
    <li>
      <a class="stretched-link" href="/competitive-research" title="" tabindex="-1"
         
        >
        Competitive Research
      </a>
      <p>Uncover valuable insights on your organic search competitors.</p>
    </li>
              
    <li>
      <a class="stretched-link" href="https://moz.com/products/pro/seo-toolbar" title="" tabindex="-1"
         
        >
        MozBar
      </a>
      <p>See top SEO metrics for free as you browse the web.</p>
    </li>
              
    <li>
      <a class="stretched-link" href="https://moz.com/free-seo-tools" title="" tabindex="-1"
         
        >
        More Free SEO Tools
      </a>
      <p>Explore all the free SEO tools Moz has to offer.</p>
    </li>
  </ul>

  <div class="mzr-ad-block mzr-links-list-ad-full">
                              <img class="" src="https://moz.com/images/cms/nav/ads/BA-290x330_TopNav-Top500-copy.png?w=290&amp;h=330&amp;auto=compress%2Cformat&amp;fit=crop&amp;dm=1691427901&amp;s=cdb705516fa34a3b118458a234eb7875" alt="What is your Brand Authority?">
        <div class="mzr-ad-copy">
                    <small class="my-1 ">Moz</small>
                    <h4 class="">What is your Brand Authority?</h4>
                            <a href="/brand-authority-quiz" title="What is your Brand Authority?" class="btn btn-yellow btn-sm btn-outline">
          Take the quiz
                  </a>
          </div>
  </div>
      
      </div>
      </li>
        <li class="mzr-nav-item mzr-nav-item-desktop mzr-dropdown mzr-megamenu">
    <a
      tabindex="4"
             class="mzr-dropdown-toggle"
                                      data-menu-order="3"
        href="/learn/seo"
              id="mzr-navbarDropdown-1025236"
        role="button"
        aria-haspopup="true"
        aria-expanded="false"
        aria-label="Learn SEO"
        data-nav-name="learn-seo"
          >Learn SEO</a>
                            
            <div class="mzr-dropdown-menu mzr-drawer-links-list "
            aria-label="Learn SEO submenu">
                

<ul class="mega-columns js-nav-links">
      
                          
    <li>
      <a class="stretched-link" href="/beginners-guide-to-seo" title="Read the Beginner&#039;s Guide" tabindex="-1"
         
        >
        Beginner&#039;s Guide to SEO
      </a>
      <p>The #1 most popular introduction to SEO, trusted by millions.</p>
    </li>
              
    <li>
      <a class="stretched-link" href="/learn/seo" title="Visit the Learning Center" tabindex="-1"
         
        >
        SEO Learning Center
      </a>
      <p>Broaden your knowledge with SEO resources for all skill levels.</p>
    </li>
              
    <li>
      <a class="stretched-link" href="/learn/seo/resources?learnContentType=webinars" title="View All Webinars" tabindex="-1"
         
        >
        On-Demand Webinars
      </a>
      <p> Learn modern SEO best practices from industry experts.</p>
    </li>
              
    <li>
      <a class="stretched-link" href="/learn/seo/resources?learnContentType=guides" title="See All SEO Guides" tabindex="-1"
         
        >
        How-To Guides
      </a>
      <p>Step-by-step guides to search success from the authority on SEO.</p>
    </li>
              
    <li>
      <a class="stretched-link" href="https://academy.moz.com/" title="Explore the Catalog" tabindex="-1"
         
        >
        Moz Academy
      </a>
      <p>Upskill and get certified with on-demand courses &amp; certifications.</p>
    </li>
              
    <li>
      <a class="stretched-link" href="https://moz.com/community/q/" title="Find SEO Answers" tabindex="-1"
         
        >
        SEO Q&amp;A
      </a>
      <p>Insights &amp; discussions from an SEO community of 500,000+.</p>
    </li>
  </ul>

  <div class="mzr-ad-block mzr-links-list-ad-full">
                              <img class="" src="https://moz.com/images/cms/nav/ads/DiscoverAPI-TopNav-290x330.png?w=290&amp;h=330&amp;auto=compress%2Cformat&amp;fit=crop&amp;dm=1717700420&amp;s=1afe03a300985200b5deebc23a4f75e0" alt="Unlock flexible pricing &amp; new endpoints">
        <div class="mzr-ad-copy">
                    <small class="my-1 text-white">The Moz API</small>
                    <h4 class="text-white">Unlock flexible pricing &amp; new endpoints</h4>
                            <a href="/products/api/pricing" title="Unlock flexible pricing &amp; new endpoints" class="btn btn-yellow btn-sm btn-outline">
          Find your plan
                  </a>
          </div>
  </div>
      
      </div>
      </li>
        <li class="mzr-nav-item mzr-nav-item-desktop ">
    <a
      tabindex="5"
      href="https://moz.com/blog"       class=""
                data-menu-order="4"
        href="/learn/seo"
          >Blog</a>
      </li>
        <li class="mzr-nav-item mzr-nav-item-desktop mzr-dropdown mzr-megamenu">
    <a
      tabindex="6"
             class="mzr-dropdown-toggle"
                                    data-menu-order="5"
        href="/about"
              id="mzr-navbarDropdown-1025242"
        role="button"
        aria-haspopup="true"
        aria-expanded="false"
        aria-label="Why Moz"
        data-nav-name="why-moz"
          >Why Moz</a>
                            
            <div class="mzr-dropdown-menu mzr-drawer-links-list "
            aria-label="Why Moz submenu">
                

<ul class="mega-columns js-nav-links">
      
                          
    <li>
      <a class="stretched-link" href="/smb-solutions" title="Grow Your Business" tabindex="-1"
         
        >
        Small Business Solutions
      </a>
      <p>Uncover insights to make smarter marketing decisions in less time.</p>
    </li>
              
    <li>
      <a class="stretched-link" href="/agency-solutions" title="Drive Client Success" tabindex="-1"
         
        >
        Agency Solutions
      </a>
      <p>Earn &amp; keep valuable clients with unparalleled data &amp; insights.</p>
    </li>
              
    <li>
      <a class="stretched-link" href="/enterprise-solutions" title="Scale Your SEO" tabindex="-1"
         
        >
        Enterprise Solutions
      </a>
      <p>Gain a competitive edge in the ever-changing world of search.</p>
    </li>
              
    <li>
      <a class="stretched-link" href="https://moz.com/about" title="Read Our Story" tabindex="-1"
         
        >
        The Moz Story
      </a>
      <p>Moz was the first &amp; remains the most trusted SEO company.</p>
    </li>
              
    <li>
      <a class="stretched-link" href="/learn/seo/resources?learnContentType=case-studies" title="See What&#039;s Possible" tabindex="-1"
         
        >
        Case Studies
      </a>
      <p>Explore how Moz drives ROI with a proven track record of success.</p>
    </li>
              
    <li>
      <a class="stretched-link" href="https://moz.com/whats-new" title="See What’s New" tabindex="-1"
         
        >
        New Releases
      </a>
      <p>Get the scoop on the latest and greatest from Moz.</p>
    </li>
  </ul>

  <div class="mzr-ad-block mzr-links-list-ad-full">
                              <img class="" src="https://moz.com/files/cms/nav/ads/CRSuite-moz-nav-outlined.svg?dm=1651020105" alt="Surface actionable competitive intel">
        <div class="mzr-ad-copy">
                    <small class="my-1 ">New Feature: Moz Pro</small>
                    <h4 class="">Surface actionable competitive intel</h4>
                            <a href="/try-competitive-research-suite" title="Surface actionable competitive intel" class="btn btn-yellow btn-sm btn-outline">
          Learn More
                  </a>
          </div>
  </div>
      
      </div>
      </li>
        </ul>
        <ul class="mzr-nav-avatar js-nav-avatar">
          

             

                
  <li class="mzr-nav-item  mzr-search">
            <a
      tabindex="7"
      title="Search"
      href="https://moz.com/search"
      class=""
            data-menu-order="6" 
          >  
  

  <svg class="icon icon-search" >
    <use href="#icon-search">
  </svg>
</a>

      </li>
             

            
  <li class="mzr-nav-item  mzr-login js-login">
            <a
      tabindex="8"
      title="Log in"
      href="/login"
      class=""
            data-menu-order="7" 
          >Log in</a>

      </li>
             

                        
  <li class="mzr-nav-item mzr-dropdown mzr-megamenu mzr-apps js-apps hidden">
            <a
      tabindex="9"
      title="Apps"
      href="#"
      class=""
            data-menu-order="8" 
              id="mzr-navbarDropdown-1026905"
        role="button"
        aria-haspopup="true"
        aria-expanded="false"
        data-mzr-dropdown=".mzr-dropdown-menu"
          >        
<svg aria-labelledby="icon-apps-grid" id="Grid_tools" data-name="Grid tools" xmlns="http://www.w3.org/2000/svg" width="19" height="19" viewBox="0 0 19 19">
  <rect id="Rectangle_1282" data-name="Rectangle 1282" width="5" height="5" fill="#fff"/>
  <rect id="Rectangle_1291" data-name="Rectangle 1291" width="5" height="5" transform="translate(0 7)"/>
  <rect id="Rectangle_1296" data-name="Rectangle 1296" width="5" height="5" transform="translate(0 7)"/>
  <rect id="Rectangle_1301" data-name="Rectangle 1301" width="5" height="5" transform="translate(0 14)"/>
  <rect id="Rectangle_1283" data-name="Rectangle 1283" width="5" height="5" transform="translate(7)"/>
  <rect id="Rectangle_1289" data-name="Rectangle 1289" width="5" height="5" transform="translate(7 7)"/>
  <rect id="Rectangle_1294" data-name="Rectangle 1294" width="5" height="5" transform="translate(7 7)"/>
  <rect id="Rectangle_1299" data-name="Rectangle 1299" width="5" height="5" transform="translate(7 14)"/>
  <rect id="Rectangle_1284" data-name="Rectangle 1284" width="5" height="5" transform="translate(7)"/>
  <rect id="Rectangle_1290" data-name="Rectangle 1290" width="5" height="5" transform="translate(7 7)"/>
  <rect id="Rectangle_1295" data-name="Rectangle 1295" width="5" height="5" transform="translate(7 7)"/>
  <rect id="Rectangle_1300" data-name="Rectangle 1300" width="5" height="5" transform="translate(7 14)"/>
  <rect id="Rectangle_1285" data-name="Rectangle 1285" width="5" height="5" transform="translate(14)"/>
  <rect id="Rectangle_1288" data-name="Rectangle 1288" width="5" height="5" transform="translate(14 7)"/>
  <rect id="Rectangle_1293" data-name="Rectangle 1293" width="5" height="5" transform="translate(14 7)"/>
  <rect id="Rectangle_1298" data-name="Rectangle 1298" width="5" height="5" transform="translate(14 14)"/>
</svg>
      </a>

          <div class="mzr-dropdown-menu" aria-labelledby="mzr-navbarDropdown-1026905">
        <ul>
                                                                      <li class="">
              <a
                tabindex="-1"
                title="Moz Pro"
                data-href="https://analytics.moz.com/pro"
                class="mzr-nav-item-logged-in"
              >Moz Pro</a>
            </li>
                                                                                                    <li class="js-local-lander">
              <a
                tabindex="-1"
                title="Moz Local"
                data-href="https://moz.com/products/local"
                class="mzr-nav-item-logged-in"
              >Moz Local</a>
            </li>
                                                                                                    <li class="hidden js-local-dashboard-only">
              <a
                tabindex="-1"
                title="Moz Local Dashboard"
                data-href="https://moz.com/login/localapp"
                class="mzr-nav-item-logged-in"
              >Moz Local Dashboard</a>
            </li>
                                                                                                    <li class="js-api-lander">
              <a
                tabindex="-1"
                title="Moz API"
                data-href="https://moz.com/products/api"
                class="mzr-nav-item-logged-in"
              >Moz API</a>
            </li>
                                                                                                  <li class="hidden js-api-dashboard-only">
              <a
                tabindex="-1"
                title="Moz API Dashboard"
                data-href="https://moz.com/api/dashboard/usage"
                class="mzr-nav-item-logged-in"
              >Moz API Dashboard</a>
            </li>
                                                                      <li class="">
              <a
                tabindex="-1"
                title="Moz Academy"
                data-href="https://academy.moz.com"
                class="mzr-nav-item-logged-in"
              >Moz Academy</a>
            </li>
                  </ul>
      </div>
      </li>
             

            
  <li class="mzr-nav-item mzr-dropdown mzr-megamenu mzr-avatar js-avatar hidden">
            <a
      tabindex="10"
      title="Avatar"
      href="#"
      class=""
            data-menu-order="9" 
              id="mzr-navbarDropdown-1025272"
        role="button"
        aria-haspopup="true"
        aria-expanded="false"
        data-mzr-dropdown=".mzr-dropdown-menu"
          >Avatar</a>

          <div class="mzr-dropdown-menu" aria-labelledby="mzr-navbarDropdown-1025272">
        <ul>
                                                                      <li class="">
              <a
                tabindex="-1"
                title="Moz Home"
                data-href="http://moz.com/home"
                class="mzr-nav-item-logged-in"
              >Moz Home</a>
            </li>
                                                                                                    <li class="">
              <a
                tabindex="-1"
                title="Notifications"
                data-href="/notifications"
                class="js-notifications mzr-nav-item-logged-in"
              >Notifications</a>
            </li>
                                                                      <li class="">
              <a
                tabindex="-1"
                title="Account &amp; Billing"
                data-href="/subscriptions"
                class="mzr-nav-item-logged-in"
              >Account &amp; Billing</a>
            </li>
                                                                      <li class="">
              <a
                tabindex="-1"
                title="Manage Users"
                data-href="/account"
                class="mzr-nav-item-logged-in"
              >Manage Users</a>
            </li>
                                                                                                    <li class="js-community-profile">
              <a
                tabindex="-1"
                title="Community Profile"
                data-href="/community/q/user/"
                class="mzr-nav-item-logged-in"
              >Community Profile</a>
            </li>
                                                                      <li class="">
              <a
                tabindex="-1"
                title="My Q&amp;A"
                data-href="/community/q/my-questions"
                class="mzr-nav-item-logged-in"
              >My Q&amp;A</a>
            </li>
                                                                      <li class="">
              <a
                tabindex="-1"
                title="My Videos"
                data-href="/videos"
                class="mzr-nav-item-logged-in"
              >My Videos</a>
            </li>
                                                                      <li class="">
              <a
                tabindex="-1"
                title="Log Out"
                data-href="/logout"
                class="mzr-nav-item-logged-in"
              >Log Out</a>
            </li>
                  </ul>
      </div>
      </li>
        </ul>
      </nav>
      <div class="mzr-mega-drawer"></div>
    </div>
  





  <script src="https://moz-static.moz.com/assets/dist/scripts/nav-a7ef64b8.min.js"></script>
<script src="https://moz-static.moz.com/assets/dist/scripts/nav-mgn-3482fba7.min.js"></script>
<script>(function() {
    var container = document.querySelector('#mzr-top-nav');
    var mozIcons = document.getElementById('moz-icons');
    if (container === null || mozIcons !== null) {
      return;
    }
    var icon = document.createElement('div');
    icon.id = 'moz-icons';
    icon.style = 'display:none;';
    document.querySelector('#mzr-top-nav').appendChild(icon);

    var request = new XMLHttpRequest();
    request.open('GET', 'https://moz.com/assets/dist/icons/icons-dc9b7dbe.min.svg', true);
    request.onload = function() {
      if (request.status >= 200 && request.status < 400) {
        var resp = request.responseText;

        document.getElementById('moz-icons').innerHTML = resp;
      }
    };
    request.send();
  })();</script>
<script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'8d2c16b3fe27689b',t:'MTcyODk1NjI5Ni4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script>
			<!-- TODO
				<nav class="navbar navbar-default navbar-fixed-top header" id="header-menu">
					<div class="container">
						<-- IMPORT partials/menu.tpl --/>
					</div>
				</nav>
			-->
		</div>
		<nav class="subnav preventSlideout">
	<div class="container" id="header-menu">
		<h3 class="subnav-title hidden-xs hidden-sm"><a href="/community/q/">The Moz Q&amp;A Forum</a></h3>
		<ul class="subnav-items">
			<li class="item visible-xs visible-sm"><a href="/community/q/">Forum</a></li>
			<li data-subnav-item="questions" class="item inactive"><a href="/community/q/questions">Questions</a></li>
			
			<li data-subnav-item="users" class="item inactive"><a href="/community/q/users">Users</a></li>
			<li class="item inactive"><a href="#" id="show_CTA">Ask the Community</a></li>
			<li class="item help">
				<a href="https://moz.com/help/guides/qa-overview/asking-question-qa">
					<svg class="icon icon-help" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="#565e66">
						<path d="M12,24C5.383,24,0,18.617,0,12S5.383,0,12,0s12,5.383,12,12S18.617,24,12,24z M12,2C6.486,2,2,6.486,2,12s4.486,10,10,10s10-4.486,10-10S17.514,2,12,2z"></path>
						<path d="M12.838,9.229c0-0.728-0.462-1.118-1.146-1.118c-0.633,0-1.095,0.337-1.557,0.816L8.75,7.614C9.52,6.656,10.598,6,11.863,6c1.932,0,3.387,0.94,3.387,3.033c0,2.2-2.566,2.857-2.361,4.967h-2.206C10.34,11.569,12.838,10.558,12.838,9.229z"></path>
						<path d="M11.781,15.5c0.72,0,1.257,0.54,1.257,1.257C13.038,17.46,12.5,18,11.781,18c-0.721,0-1.243-0.54-1.243-1.243C10.538,16.04,11.06,15.5,11.781,15.5z"></path>
					</svg>
				</a>
			</li>
		</ul>
	</div>
</nav>
		<section class="hero">
	<div class="container">
		<h1 class="hero-title">
			<p>Welcome to the Q&A Forum</p>
		</h1>
		<h4 class="hero-subtitle">
			<p>Browse the forum for helpful insights and fresh discussions about all things SEO.</p>
		</h4>
	</div>
</section>
		<div class="container" id="content">
		<noscript>
    <div class="alert alert-danger">
        <p>
            Your browser does not seem to support JavaScript. As a result, your viewing experience will be diminished, and you have been placed in <strong>read-only mode</strong>.
        </p>
        <p>
            Please download a browser that supports JavaScript, or enable it if it's disabled (i.e. NoScript).
        </p>
    </div>
</noscript>
		
<script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "QAPage",
    "mainEntity": {
      "@type": "Question",
      "name": "Pages with excessive number of links",
      "text": "<p dir=\"auto\">Hi all, I work for a retailer and I've crawled our website with RankTracker for optimization suggestions.</p>
<p dir=\"auto\">The main suggestion is \"Pages with excessive number of links: 4178\"</p>
<p dir=\"auto\">The page with the largest amount of links has 634 links (627 internal, 7 external), the lowest 382 links (375 internal, 7 external).</p>
<p dir=\"auto\">However, when I view the source on any one of the example pages, it becomes obvious that the site's main navigation header contains 358 links, so every new page starts with 358 links before any content.</p>
<p dir=\"auto\">Our rivals and much larger sites like <a href=\"http://argos.co.uk\" rel=\"nofollow ugc\">argos.co.uk</a> appear to have just as many links in their main navigation menu.</p>
<p dir=\"auto\">So my questions are:</p>
<p dir=\"auto\">1. Will these excessive links really be causing us a problem or is it just 'good practice' to have fewer links<br />
2. Can I use 'no follow' to stop Google etc from counting the 358 main navigation links<br />
3. Is have 4000+ pages of your website all dumbly pointing to other pages a help or hindrance?<br />
4. Can we 'minify' this code so it's cached on first load and therefore loads faster?</p>
<p dir=\"auto\">Thank you.</p>
",
      "url": "",
      "answerCount": 2,
      "upvoteCount": 0,
      "dateCreated": "2016-02-17T07:10:59.000Z",
      "author": {
        "@type": "Person",
        "name": "Bee159",
        "url": "/community/q/user/bee159"
      },
      "acceptedAnswer": [
        
      ],
      "suggestedAnswer": [
        
        {
          "@type": "Answer",
          "text": "<p dir=\"auto\">Pre 2013 it was bad practice to have in excess of 100 links per page, google technical guideline.  Many SEO tools still use it as a warning bell. However Matt Cutts from google - I recall a few years ago - came out and categorically said it is NOT bad practice.  Have as many links as you like as long as it is natural and helps the customer.</p>
<p dir=\"auto\">What Matt did say is if it appears like spam, them google will penalize you accordingly. Here we go just found the video. <a href=\"https://www.youtube.com/watch?v=QHG6BkmzDEM\" rel=\"nofollow ugc\">https://www.youtube.com/watch?v=QHG6BkmzDEM</a></p>
<p dir=\"auto\">So to be clear - if the links are needed and help the customer - I would not concern myself.  Watch the video, nothing better than going straight to the source.</p>
<p dir=\"auto\">Hope that assists</p>
",
          "dateCreated": "2016-02-17T08:30:44.000Z",
          "url": "/community/q/post/288601",
          "author": {
            "@type": "Person",
            "name": "ClaytonJ",
            "url": "/community/q/user/claytonj"
          },
          "upvoteCount": 1
        }
	    	
      ]
    }
  }
</script>

<ol class="breadcrumb" itemscope="itemscope" itemprop="breadcrumb" itemtype="http://schema.org/BreadcrumbList">
	
	<li itemscope="itemscope" itemprop="itemListElement" itemtype="http://schema.org/ListItem" >
		<meta itemprop="position" content="0" />
		<a href="/community/q/" itemprop="item">
			<span itemprop="name">
				Home
				
			</span>
		</a>
	</li>
	
	<li itemscope="itemscope" itemprop="itemListElement" itemtype="http://schema.org/ListItem" >
		<meta itemprop="position" content="1" />
		<a href="/community/q/category/9/seo-tactics" itemprop="item">
			<span itemprop="name">
				SEO Tactics
				
			</span>
		</a>
	</li>
	
	<li itemscope="itemscope" itemprop="itemListElement" itemtype="http://schema.org/ListItem" >
		<meta itemprop="position" content="2" />
		<a href="/community/q/category/16/intermediate-advanced-seo" itemprop="item">
			<span itemprop="name">
				Intermediate &amp; Advanced SEO
				
			</span>
		</a>
	</li>
	
	<li component="breadcrumb/current" itemscope="itemscope" itemprop="itemListElement" itemtype="http://schema.org/ListItem" class="active">
		<meta itemprop="position" content="3" />
		
			<span itemprop="name">
				Pages with excessive number of links
				
				
				
			</span>
		
	</li>
	
</ol>



<div data-widget-area="header">
	
</div>

<div class="row">
	<div class="topic col-lg-8 col-sm-12" itemid="/community/q/topic/58032/pages-with-excessive-number-of-links/3" itemscope itemtype="https://schema.org/DiscussionForumPosting">
		<meta itemprop="datePublished" content="2016-02-17T07:10:59.000Z">
		<meta itemprop="dateModified" content="2016-02-17T08:48:15.000Z">
		<meta itemprop="author" itemscope itemtype="https://schema.org/Person" itemref="topicAuthorName topicAuthorUrl">
		<meta id="topicAuthorName" itemprop="name" content="Bee159">
		<meta id="topicAuthorUrl" itemprop="url" content="/community/q/user/bee159">
		<div class="topic-header">
			<h3 component="post/header" class="" itemprop="name">
				<span class="topic-title" component="topic/title">
					<span component="topic/labels">
						<i component="topic/pinned" class="fa fa-thumb-tack hidden" title="Pinned"></i>
						<i component="topic/locked" class="fa fa-lock " title="Locked"></i>
						<i class="fa fa-arrow-circle-right hidden" title="Moved"></i>
						
					</span>
					Pages with excessive number of links
				</span>
			</h3>

			<div class="topic-info clearfix">
				<div class="category-item inline-block">
					<div role="presentation" class="icon pull-left" style="background-color: #fc4949; color: #FFFFFF;">
						<i class="fa fa-fw fa-graduation-cap"></i>
					</div>
					<a href="/community/q/category/16/intermediate-advanced-seo">Intermediate &amp; Advanced SEO</a>
				</div>

				<div class="tags tag-list inline-block hidden-xs">
					
				</div>
				<div class="inline-block hidden-xs">
					<div class="stats text-muted">
	<i class="fa fa-fw fa-user" title="Posters"></i>
	<span title="3" class="human-readable-number">3</span>
</div>
<div class="stats text-muted">
	<i class="fa fa-fw fa-pencil" title="Posts"></i>
	<span component="topic/post-count" title="3" class="human-readable-number">3</span>
</div>
<div class="stats text-muted">
	<i class="fa fa-fw fa-eye" title="Views"></i>
	<span class="human-readable-number" title="1925">1925</span>
</div>
				</div>
				
				<!-- This partial intentionally left blank; overwritten by nodebb-plugin-browsing-users -->

				<div class="topic-main-buttons pull-right inline-block">
	<span class="loading-indicator btn pull-left hidden" done="0">
		<span class="hidden-xs">Loading More Posts</span> <i class="fa fa-refresh fa-spin"></i>
	</span>

	

	

	<div title="Sort by" class="btn-group bottom-sheet hidden-xs" component="thread/sort">
	<button class="btn btn-sm btn-default dropdown-toggle" data-toggle="dropdown" type="button">
	<span><i class="fa fa-fw fa-sort"></i></span></button>
	<ul class="dropdown-menu dropdown-menu-right">
		<li><a href="#" class="oldest_to_newest" data-sort="oldest_to_newest"><i class="fa fa-fw"></i> Oldest to Newest</a></li>
		<li><a href="#" class="newest_to_oldest" data-sort="newest_to_oldest"><i class="fa fa-fw"></i> Newest to Oldest</a></li>
		<li><a href="#" class="most_votes" data-sort="most_votes"><i class="fa fa-fw"></i> Most Votes</a></li>
	</ul>
</div>


	<div class="inline-block">
	
	</div>
	<div component="topic/reply/container" class="btn-group action-bar bottom-sheet hidden">
	<a href="/community/q/compose?tid=58032&title=Pages with excessive number of links" class="btn btn-sm btn-primary" component="topic/reply" data-ajaxify="false" role="button"><i class="fa fa-reply visible-xs-inline"></i><span class="visible-sm-inline visible-md-inline visible-lg-inline"> Reply</span></a>
	<button type="button" class="btn btn-sm btn-primary dropdown-toggle" data-toggle="dropdown">
		<span class="caret"></span>
	</button>
	<ul class="dropdown-menu pull-right" role="menu">
		<li><a href="#" component="topic/reply-as-topic">Reply as question</a></li>
	</ul>
</div>




<a component="topic/reply/guest" href="/community/q/login" class="btn btn-sm btn-primary">Log in to reply</a>


</div>

			</div>
		</div>
		

		
		<div component="topic/deleted/message" class="alert alert-warning hidden clearfix">
    <span class="pull-left">This topic has been deleted. Only users with question management privileges can see it.</span>
    <span class="pull-right">
        
    </span>
</div>
		

		<ul component="topic" class="posts timeline" data-tid="58032" data-cid="16">
			
				<li component="post" class="  topic-owner-post" data-index="0" data-pid="58032" data-uid="101325" data-timestamp="1455693059000" data-username="Bee159" data-userslug="bee159" itemprop="comment" itemscope itemtype="http://schema.org/Comment"
>
					<a component="post/anchor" data-index="0" id="0"></a>

					<meta itemprop="datePublished" content="2016-02-17T07:10:59.000Z">
					<meta itemprop="dateModified" content="">

					<div class="clearfix post-header">
	<div class="icon pull-left">
		<a href="/community/q/user/bee159">
			<img class="avatar  avatar-sm2x avatar-rounded" alt="Bee159" title="Bee159" data-uid="101325" loading="lazy" component="user/picture" src="/community/q/assets/uploads/profile/101325-profileavatar-1619582721754.png" style="" />
			<i component="user/status" class="fa fa-circle status offline" title="Offline"></i>
		</a>
	</div>

	<small class="pull-left" itemprop="author" itemscope itemtype="https://schema.org/Person">
		<meta itemprop="name" content="Bee159">
		<meta itemprop="url" content="/community/q/user/bee159">

		<strong>
			<a href="/community/q/user/bee159" data-username="Bee159" data-uid="101325">Bee159</a>
		</strong>

		

		

		<span class="visible-xs-inline-block visible-sm-inline-block visible-md-inline-block visible-lg-inline-block">
				

				<span>
						
				</span>
		</span>

	</small>
	<small class="pull-right">
		<span class="bookmarked"><i class="fa fa-bookmark-o"></i></span>
	</small>
	<small class="pull-right">
		<i component="post/edit-indicator" class="fa fa-pencil-square edit-icon hidden"></i>

		<small data-editor="" component="post/editor" class="hidden">last edited by  <span class="timeago" title=""></span></small>

		<span class="visible-xs-inline-block visible-sm-inline-block visible-md-inline-block visible-lg-inline-block">
				<a class="permalink" href="/community/q/post/58032"><span class="timeago" title="2016-02-17T07:10:59.000Z"></span></a>
		</span>
	</small>
</div>

<br />

<div class="content" component="post/content" itemprop="text">
	<p dir="auto">Hi all, I work for a retailer and I've crawled our website with RankTracker for optimization suggestions.</p>
<p dir="auto">The main suggestion is "Pages with excessive number of links: 4178"</p>
<p dir="auto">The page with the largest amount of links has 634 links (627 internal, 7 external), the lowest 382 links (375 internal, 7 external).</p>
<p dir="auto">However, when I view the source on any one of the example pages, it becomes obvious that the site's main navigation header contains 358 links, so every new page starts with 358 links before any content.</p>
<p dir="auto">Our rivals and much larger sites like <a href="http://argos.co.uk" rel="nofollow ugc">argos.co.uk</a> appear to have just as many links in their main navigation menu.</p>
<p dir="auto">So my questions are:</p>
<p dir="auto">1. Will these excessive links really be causing us a problem or is it just 'good practice' to have fewer links<br />
2. Can I use 'no follow' to stop Google etc from counting the 358 main navigation links<br />
3. Is have 4000+ pages of your website all dumbly pointing to other pages a help or hindrance?<br />
4. Can we 'minify' this code so it's cached on first load and therefore loads faster?</p>
<p dir="auto">Thank you.</p>

</div>

<div class="post-footer">
	

	<div class="clearfix">
	
	<a component="post/reply-count" data-target-component="post/replies/container" href="#" class="threaded-replies no-select pull-left hidden">
		<span component="post/reply-count/avatars" class="avatars ">
				
		</span>

		<span class="replies-count" component="post/reply-count/text" data-replies="0">1 Reply</span>
		<span class="replies-last hidden-xs">Last reply <span class="timeago" title=""></span></span>

		<i class="fa fa-fw fa-chevron-right" component="post/replies/open"></i>
		<i class="fa fa-fw fa-chevron-down hidden" component="post/replies/close"></i>
		<i class="fa fa-fw fa-spin fa-spinner hidden" component="post/replies/loading"></i>
	</a>
	

	<small class="pull-right">
		<!-- This partial intentionally left blank; overwritten by nodebb-plugin-reactions -->
		<span class="post-tools">
				<a component="post/reply" href="#" class="no-select hidden">Reply</a>
				<a component="post/quote" href="#" class="no-select hidden">Quote</a>
		</span>

		
		<span class="votes">
				<a component="post/upvote" href="#" class="">
						<i class="fa fa-chevron-up"></i>
				</a>

				<span component="post/vote-count" data-votes="0">0</span>

				
		</span>
		

		<span component="post/tools" class="dropdown moderator-tools bottom-sheet ">
	<a href="#" data-toggle="dropdown" data-ajaxify="false"><i class="fa fa-fw fa-ellipsis-v"></i></a>
	<ul class="dropdown-menu dropdown-menu-right hidden" role="menu"></ul>
</span>

	</small>
	</div>
	<div component="post/replies/container"></div>
</div>

				</li>
			
				<li component="post" class="  " data-index="1" data-pid="288602" data-uid="35115" data-timestamp="1455698895000" data-username="netzkern_AG" data-userslug="netzkern_ag" itemprop="comment" itemscope itemtype="http://schema.org/Comment"
>
					<a component="post/anchor" data-index="1" id="1"></a>

					<meta itemprop="datePublished" content="2016-02-17T08:48:15.000Z">
					<meta itemprop="dateModified" content="2016-02-17T15:16:30.000Z">

					<div class="clearfix post-header">
	<div class="icon pull-left">
		<a href="/community/q/user/netzkern_ag">
			<img class="avatar  avatar-sm2x avatar-rounded" alt="netzkern_AG" title="netzkern_AG" data-uid="35115" loading="lazy" component="user/picture" src="https://moz.com/avatar/large/5/n.png"></img>
			<i component="user/status" class="fa fa-circle status offline" title="Offline"></i>
		</a>
	</div>

	<small class="pull-left" itemprop="author" itemscope itemtype="https://schema.org/Person">
		<meta itemprop="name" content="netzkern_AG">
		<meta itemprop="url" content="/community/q/user/netzkern_ag">

		<strong>
			<a href="/community/q/user/netzkern_ag" data-username="netzkern_AG" data-uid="35115">netzkern_AG</a>
		</strong>

		

<a href="/community/q/groups/qa_subscriber"><small class="label group-label inline-block" style="color:#ffffff;background-color: #4dbdeb;"><i class="fa fa-check-circle"></i> Subscriber</small></a>



		

		<span class="visible-xs-inline-block visible-sm-inline-block visible-md-inline-block visible-lg-inline-block">
				

				<span>
						
				</span>
		</span>

	</small>
	<small class="pull-right">
		<span class="bookmarked"><i class="fa fa-bookmark-o"></i></span>
	</small>
	<small class="pull-right">
		<i component="post/edit-indicator" class="fa fa-pencil-square edit-icon hidden"></i>

		<small data-editor="" component="post/editor" class="hidden">last edited by  <span class="timeago" title="2016-02-17T15:16:30.000Z"></span></small>

		<span class="visible-xs-inline-block visible-sm-inline-block visible-md-inline-block visible-lg-inline-block">
				<a class="permalink" href="/community/q/post/288602"><span class="timeago" title="2016-02-17T08:48:15.000Z"></span></a>
		</span>
	</small>
</div>

<br />

<div class="content" component="post/content" itemprop="text">
	<p dir="auto">There has even been a Google Webmaster Guidelines Update in February 2016 which states</p>
<p dir="auto">"Limit the number of links on a page to a reasonable number <strong>(a few thousand at most</strong>)."  (Source: <a href="https://support.google.com/webmasters/answer/35769?hl=en" rel="nofollow ugc">https://support.google.com/webmasters/answer/35769?hl=en</a>)</p>
<p dir="auto">So I really would not bother too much, especially not in a navigation - it often makes lots of sense to have lots of links there. (For example I have several alphabetical selections available on hover from main categories. It would not make sense to remove them just to have fewer links.)</p>
<p dir="auto">More links are of course not always better - consider what the user is likely to expect/need in navigation etc. Of course, more links mean that the relative importance of each link decreases; but google is able to identify navigation and repeating elements that appear on every page. I'd assume that they treat them different to main-content links. Because, well, they feel a lot different.</p>
<p dir="auto">Regards</p>
<p dir="auto">Nico</p>

</div>

<div class="post-footer">
	

	<div class="clearfix">
	
	<a component="post/reply-count" data-target-component="post/replies/container" href="#" class="threaded-replies no-select pull-left hidden">
		<span component="post/reply-count/avatars" class="avatars ">
				
		</span>

		<span class="replies-count" component="post/reply-count/text" data-replies="0">1 Reply</span>
		<span class="replies-last hidden-xs">Last reply <span class="timeago" title=""></span></span>

		<i class="fa fa-fw fa-chevron-right" component="post/replies/open"></i>
		<i class="fa fa-fw fa-chevron-down hidden" component="post/replies/close"></i>
		<i class="fa fa-fw fa-spin fa-spinner hidden" component="post/replies/loading"></i>
	</a>
	

	<small class="pull-right">
		<!-- This partial intentionally left blank; overwritten by nodebb-plugin-reactions -->
		<span class="post-tools">
				<a component="post/reply" href="#" class="no-select hidden">Reply</a>
				<a component="post/quote" href="#" class="no-select hidden">Quote</a>
		</span>

		
		<span class="votes">
				<a component="post/upvote" href="#" class="">
						<i class="fa fa-chevron-up"></i>
				</a>

				<span component="post/vote-count" data-votes="1">1</span>

				
		</span>
		

		<span component="post/tools" class="dropdown moderator-tools bottom-sheet ">
	<a href="#" data-toggle="dropdown" data-ajaxify="false"><i class="fa fa-fw fa-ellipsis-v"></i></a>
	<ul class="dropdown-menu dropdown-menu-right hidden" role="menu"></ul>
</span>

	</small>
	</div>
	<div component="post/replies/container"></div>
</div>

				</li>
			
				<li component="post" class="  " data-index="2" data-pid="288601" data-uid="77292" data-timestamp="1455697844000" data-username="ClaytonJ" data-userslug="claytonj" itemprop="comment" itemscope itemtype="http://schema.org/Comment"
>
					<a component="post/anchor" data-index="2" id="2"></a>

					<meta itemprop="datePublished" content="2016-02-17T08:30:44.000Z">
					<meta itemprop="dateModified" content="2016-02-17T08:43:02.000Z">

					<div class="clearfix post-header">
	<div class="icon pull-left">
		<a href="/community/q/user/claytonj">
			<img class="avatar  avatar-sm2x avatar-rounded" alt="ClaytonJ" title="ClaytonJ" data-uid="77292" loading="lazy" component="user/picture" src="/community/q/assets/uploads/profile/77292-profileavatar-1619582671334.png" style="" />
			<i component="user/status" class="fa fa-circle status offline" title="Offline"></i>
		</a>
	</div>

	<small class="pull-left" itemprop="author" itemscope itemtype="https://schema.org/Person">
		<meta itemprop="name" content="ClaytonJ">
		<meta itemprop="url" content="/community/q/user/claytonj">

		<strong>
			<a href="/community/q/user/claytonj" data-username="ClaytonJ" data-uid="77292">ClaytonJ</a>
		</strong>

		

		

		<span class="visible-xs-inline-block visible-sm-inline-block visible-md-inline-block visible-lg-inline-block">
				

				<span>
						
				</span>
		</span>

	</small>
	<small class="pull-right">
		<span class="bookmarked"><i class="fa fa-bookmark-o"></i></span>
	</small>
	<small class="pull-right">
		<i component="post/edit-indicator" class="fa fa-pencil-square edit-icon hidden"></i>

		<small data-editor="" component="post/editor" class="hidden">last edited by  <span class="timeago" title="2016-02-17T08:43:02.000Z"></span></small>

		<span class="visible-xs-inline-block visible-sm-inline-block visible-md-inline-block visible-lg-inline-block">
				<a class="permalink" href="/community/q/post/288601"><span class="timeago" title="2016-02-17T08:30:44.000Z"></span></a>
		</span>
	</small>
</div>

<br />

<div class="content" component="post/content" itemprop="text">
	<p dir="auto">Pre 2013 it was bad practice to have in excess of 100 links per page, google technical guideline.  Many SEO tools still use it as a warning bell. However Matt Cutts from google - I recall a few years ago - came out and categorically said it is NOT bad practice.  Have as many links as you like as long as it is natural and helps the customer.</p>
<p dir="auto">What Matt did say is if it appears like spam, them google will penalize you accordingly. Here we go just found the video. <a href="https://www.youtube.com/watch?v=QHG6BkmzDEM" rel="nofollow ugc">https://www.youtube.com/watch?v=QHG6BkmzDEM</a></p>
<p dir="auto">So to be clear - if the links are needed and help the customer - I would not concern myself.  Watch the video, nothing better than going straight to the source.</p>
<p dir="auto">Hope that assists</p>

</div>

<div class="post-footer">
	

	<div class="clearfix">
	
	<a component="post/reply-count" data-target-component="post/replies/container" href="#" class="threaded-replies no-select pull-left hidden">
		<span component="post/reply-count/avatars" class="avatars ">
				
		</span>

		<span class="replies-count" component="post/reply-count/text" data-replies="0">1 Reply</span>
		<span class="replies-last hidden-xs">Last reply <span class="timeago" title=""></span></span>

		<i class="fa fa-fw fa-chevron-right" component="post/replies/open"></i>
		<i class="fa fa-fw fa-chevron-down hidden" component="post/replies/close"></i>
		<i class="fa fa-fw fa-spin fa-spinner hidden" component="post/replies/loading"></i>
	</a>
	

	<small class="pull-right">
		<!-- This partial intentionally left blank; overwritten by nodebb-plugin-reactions -->
		<span class="post-tools">
				<a component="post/reply" href="#" class="no-select hidden">Reply</a>
				<a component="post/quote" href="#" class="no-select hidden">Quote</a>
		</span>

		
		<span class="votes">
				<a component="post/upvote" href="#" class="">
						<i class="fa fa-chevron-up"></i>
				</a>

				<span component="post/vote-count" data-votes="1">1</span>

				
		</span>
		

		<span component="post/tools" class="dropdown moderator-tools bottom-sheet ">
	<a href="#" data-toggle="dropdown" data-ajaxify="false"><i class="fa fa-fw fa-ellipsis-v"></i></a>
	<ul class="dropdown-menu dropdown-menu-right hidden" role="menu"></ul>
</span>

	</small>
	</div>
	<div component="post/replies/container"></div>
</div>

				</li>
			
		</ul>

		

		
		<div component="pagination" class="text-center pagination-container hidden">
	<ul class="pagination hidden-xs">
		<li class="previous pull-left disabled">
			<a href="?" data-page="1"><i class="fa fa-chevron-left"></i> </a>
		</li>

		

		<li class="next pull-right disabled">
			<a href="?" data-page="1"> <i class="fa fa-chevron-right"></i></a>
		</li>
	</ul>

	<ul class="pagination hidden-sm hidden-md hidden-lg">
		<li class="first disabled">
			<a href="?" data-page="1"><i class="fa fa-fast-backward"></i> </a>
		</li>

		<li class="previous disabled">
			<a href="?" data-page="1"><i class="fa fa-chevron-left"></i> </a>
		</li>

		<li component="pagination/select-page" class="page select-page">
			<a href="#">1 / 1</a>
		</li>

		<li class="next disabled">
			<a href="?" data-page="1"> <i class="fa fa-chevron-right"></i></a>
		</li>

		<li class="last disabled">
			<a href="?" data-page="1"><i class="fa fa-fast-forward"></i> </a>
		</li>
	</ul>
</div>
		

		<div class="pagination-block text-center">
    <div class="progress-bar"></div>
    <div class="wrapper dropup">
        <i class="fa fa-2x fa-angle-double-up pointer fa-fw pagetop"></i>

        <a href="#" class="dropdown-toggle" data-toggle="dropdown">
            <span class="pagination-text"></span>
        </a>

        <i class="fa fa-2x fa-angle-double-down pointer fa-fw pagebottom"></i>
        <ul class="dropdown-menu dropdown-menu-right" role="menu">
            <li>
                <div class="row">
                    <div class="col-xs-8 post-content"></div>
                    <div class="col-xs-4 text-right">
                        <div class="scroller-content">
                            <span class="pointer pagetop">First post <i class="fa fa-angle-double-up"></i></span>
                            <div class="scroller-container">
                                <div class="scroller-thumb">
                                    <span class="thumb-text"></span>
                                    <div class="scroller-thumb-icon"></div>
                                </div>
                            </div>
                            <span class="pointer pagebottom">Last post <i class="fa fa-angle-double-down"></i></span>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-xs-6">
                        <button id="myNextPostBtn" class="btn btn-default form-control" disabled>Go to my next post</button>
                    </div>
                    <div class="col-xs-6">
                        <input type="number" class="form-control" id="indexInput" placeholder="Enter index">
                    </div>
                </div>
            </li>
        </ul>
    </div>
</div>

	</div>
	<div data-widget-area="sidebar" class="col-lg-4 col-sm-12">
		
<div class="alert alert-warning etiquette text-center">
	<h3>Got a burning SEO question?</h3>
	<p>Subscribe to Moz Pro to gain full access to Q&A, answer questions, and ask your own.</p>
	<br />
	<p><a href="https://moz.com/checkout/freetrial?source=qa" class="btn button button-yellow button-large button-3d">Start my free trial</a></p><br />
</div>


<div class="side-box">
	<div class="search">
		<form id="search-form" accept-charset="UTF-8" method="get" action="/search">
			<label class="sans-serif-label" for="query">Have a Question?</label>
			<div class="input-append" id="search-fields">
				<input autocomplete="off" class="span3" id="query" name="query" placeholder="Search the Q&amp;A forum" type="text">
				<input class="btn btn-default btn-sm button span1" name="term" type="submit" value="Search">
			</div>
		</form>

		<div id="quick-search-container" class="quick-search-container hidden">
			<div class="checkbox filter-category">
				<label>
					<input type="checkbox" checked><span class="name"></span>
				</label>
			</div>
			<div class="text-center loading-indicator"><i class="fa fa-spinner fa-spin"></i></div>
			<div class="quick-search-results-container"></div>
		</div>
	</div>
</div>

<div class="side-box">
	<h4>Browse Questions</h4>

	<div class="list-filters" data-component="sidebar/filters">
    	<form>
			<div class="form-body">
				<div class="filter-row">
					<label for="view">View</label>
					<select class="filter span3" id="view" name="view">
						<option value="all" selected="selected">All Questions</option>
						<!-- TODO <option value="featured">Bounty</option> -->
						<option value="new">New (No Responses)</option>
						<option value="discussion">Discussion</option>
						<option value="answered">Answered</option>
						<option value="support">Product Support</option>
						<option value="unanswered">Unanswered</option>
					</select>
				</div>
				<div class="filter-row">
					<label for="from">From</label>
					<select class="filter span3" id="from" name="from">
						<option value="all" selected="selected">All Time</option>
						<option value="last_30_days">Last 30 Days</option>
						<option value="last_7_days">Last 7 Days</option>
						<option value="last_24_hours">Last 24 Hours</option>
					</select>
				</div>
				<div class="filter-row">
					<label for="sort">Sorted by</label>
					<select class="filter span3" id="sort" name="sort">
						<option value="newest" selected="selected">Latest Questions</option>
						<option value="activity">Recent Activity</option>
						<option value="most_popular">Most Thumbs Up</option>
						<option value="most_responses">Most Responses</option>
						<option value="least_responses">Fewest Responses</option>
						<option value="oldest">Oldest Questions</option>
					</select>
				</div>
				<div class="filter-row">
					<label for="category">With category</label>
					<select class="filter span3" id="category" name="category" data-component="sidebar/filter/category">
						<option value="all" selected="}">All Categories</option>
						
						<option value="33" >Affiliate Marketing</option>
						
						<option value="23" >Algorithm Updates</option>
						
						<option value="56" >API</option>
						
						<option value="31" >Branding</option>
						
						<option value="3" >Community</option>
						
						<option value="19" >Competitive Research</option>
						
						<option value="10" >Content Development</option>
						
						<option value="34" >Conversion Rate Optimization</option>
						
						<option value="7" >Digital Marketing</option>
						
						<option value="63" >Feature Requests</option>
						
						<option value="53" >Getting Started</option>
						
						<option value="14" >Image &amp; Video Optimization</option>
						
						<option value="40" >Industry Events</option>
						
						<option value="44" >Industry News</option>
						
						<option value="16" selected="selected">Intermediate &amp; Advanced SEO</option>
						
						<option value="22" >International SEO</option>
						
						<option value="43" >Jobs and Opportunities</option>
						
						<option value="64" >Keyword Explorer</option>
						
						<option value="12" >Keyword Research</option>
						
						<option value="13" >Link Building</option>
						
						<option value="55" >Link Explorer</option>
						
						<option value="59" >Local Listings</option>
						
						<option value="5" >Local SEO</option>
						
						<option value="58" >Local Website Optimization</option>
						
						<option value="52" >Moz Bar</option>
						
						<option value="54" >Moz Local</option>
						
						<option value="48" >Moz News</option>
						
						<option value="46" >Moz Pro</option>
						
						<option value="47" >Moz Tools</option>
						
						<option value="11" >On-Page Optimization</option>
						
						<option value="71" >Other SEO Tools</option>
						
						<option value="29" >Paid Search Marketing</option>
						
						<option value="49" >Product Support</option>
						
						<option value="6" >Reporting &amp; Analytics</option>
						
						<option value="8" >Research &amp; Trends</option>
						
						<option value="60" >Reviews and Ratings</option>
						
						<option value="21" >Search Behavior</option>
						
						<option value="9" >SEO Tactics</option>
						
						<option value="26" >SERP Trends</option>
						
						<option value="27" >Social Media</option>
						
						<option value="15" >Technical SEO</option>
						
						<option value="25" >Web Design</option>
						
						<option value="24" >White Hat &#x2F; Black Hat SEO</option>
						
					</select>
				</div>
			</div>
			<div class="form-actions text-right">
				<input class="btn btn-sm btn-default button" type="submit" value="Filter questions">
			</div>
		</form>
	</div>
</div>

		
		<div class="side-box"><div class="panel-heading"><h4>Explore more categories</h4></div><div class="panel-body">
<ul class="categories-list">
	<li>
		
		<h4><a href="/community/q/category/47/moz-tools">Moz Tools</a></h4>
		
		<p><p dir="auto">Chat with the community about the Moz tools.</p>
</p>
	</li>
</ul>

<ul class="categories-list">
	<li>
		
		<h4><a href="/community/q/category/9/seo-tactics">SEO Tactics</a></h4>
		
		<p><p dir="auto">Discuss the SEO process with fellow marketers</p>
</p>
	</li>
</ul>

<ul class="categories-list">
	<li>
		
		<h4><a href="/community/q/category/3/community">Community</a></h4>
		
		<p><p dir="auto">Discuss industry events, jobs, and news!</p>
</p>
	</li>
</ul>

<ul class="categories-list">
	<li>
		
		<h4><a href="/community/q/category/7/digital-marketing">Digital Marketing</a></h4>
		
		<p><p dir="auto">Chat about tactics outside of SEO</p>
</p>
	</li>
</ul>

<ul class="categories-list">
	<li>
		
		<h4><a href="/community/q/category/8/research-trends">Research &amp; Trends</a></h4>
		
		<p><p dir="auto">Dive into research and trends in the search industry.</p>
</p>
	</li>
</ul>

<ul class="categories-list">
	<li>
		
		<h4><a href="/community/q/category/4/support">Support</a></h4>
		
		<p><p dir="auto">Connect on product support and feature requests.</p>
</p>
	</li>
</ul>

<ul class="categories-list">
	<li>
		
		<h4><a href="https:&#x2F;&#x2F;moz.com&#x2F;community&#x2F;q&#x2F;categories">See all categories</a></h4>
		
		<p></p>
	</li>
</ul>
</div></div>
		
		<div class="topics-list">
	<h4>Related Questions</h4>
	<div class="category">
		<ul component="category" class="topic-list" itemscope itemtype="http://www.schema.org/ItemList" data-nextstart="" data-set="">
	<meta itemprop="itemListOrder" content="descending">
	
	<li component="category/topic" class="clearfix category-item locked unread " data-tid="63188" data-index="0" data-cid="16" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
		<link itemprop="url" content="/community/q/topic/63188/link-types-for-link-building" />
		<meta itemprop="name" content="Link Types For Link Building" />
		<meta itemprop="itemListOrder" content="descending" />
		<meta itemprop="position" content="1" />
		<a id="0" data-index="0" component="topic/anchor"></a>

		<div class="content">
			<div class="avatar pull-left">
				

				
				<a href="/community/q/user/spyaccounts14" class="pull-left">
					
					<img class="avatar not-responsive avatar-rounded" alt="spyaccounts14" title="spyaccounts14" data-uid="132358" loading="lazy" component="avatar/icon" src="https://moz.com/avatar/large/8/s.png"></img>
					
				</a>
				
			</div>

			<h3 component="topic/header" class="title">
				<i component="topic/pinned" class="fa fa-thumb-tack hide" title="Pinned"></i>
				<i component="topic/locked" class="fa fa-lock " title="Locked"></i>
				<i component="topic/moved" class="fa fa-arrow-circle-right hide" title="Moved"></i>
				

				
				<a href="/community/q/topic/63188/link-types-for-link-building/6" itemprop="url">Link Types For Link Building</a><br />
				
			</h3>

			

			<div class="category-content">
				
				<p dir="auto">Hi i have a SEO agency we work with who are building quality guest post links for us, however they are also building forum, profile, blog comments <br />
and directory based links.
60% of their links they are building are high quality, relevant guest posts while the other 40% are the other link types.
The 40% seem to be relevant directories, forums, blog comments, etc.
They said they build other link types because it diversifies the link building and profile rather then just building high quality guest posts.
As just building one link type can leave a footprint.
What are your thoughts on this?
Cheers.
</p>
				
				
				<small class="category-name">
					<a href="/community/q/category/16/intermediate-advanced-seo"><span class="fa-stack fa-lg" style="background-color: #fc4949; color: #FFFFFF;"><i style="color:#FFFFFF;" class="fa fa-graduation-cap fa-stack-1x"></i></span> Intermediate &amp; Advanced SEO</a> |
				</small>
				

				<small>
					
					<span class="timeago" title="2017-05-03T12:19:21.000Z"></span>
					| <a href="/community/q/user/spyaccounts14">spyaccounts14</a>
					
				</small>
			</div>

			
			<div class="votes" title="Votes">
				<i class="fa fa-thumbs-up"></i> <span class="human-readable-number" title="0">0</span>
			</div>
			
		</div>
	</li>
	
	<li component="category/topic" class="clearfix category-item locked unread " data-tid="58722" data-index="1" data-cid="16" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
		<link itemprop="url" content="/community/q/topic/58722/seo-implication-of-adding-large-number-of-new-product-pages" />
		<meta itemprop="name" content="SEO implication of adding large number of new product pages" />
		<meta itemprop="itemListOrder" content="descending" />
		<meta itemprop="position" content="2" />
		<a id="1" data-index="1" component="topic/anchor"></a>

		<div class="content">
			<div class="avatar pull-left">
				

				
				<a href="/community/q/user/dhs_sh" class="pull-left">
					
					<img class="avatar not-responsive avatar-rounded" alt="DHS_SH" title="DHS_SH" data-uid="39447" loading="lazy" component="avatar/icon" src="https://moz.com/avatar/large/7/d.png"></img>
					
				</a>
				
			</div>

			<h3 component="topic/header" class="title">
				<i component="topic/pinned" class="fa fa-thumb-tack hide" title="Pinned"></i>
				<i component="topic/locked" class="fa fa-lock " title="Locked"></i>
				<i component="topic/moved" class="fa fa-arrow-circle-right hide" title="Moved"></i>
				

				
				<a href="/community/q/topic/58722/seo-implication-of-adding-large-number-of-new-product-pages/4" itemprop="url">SEO implication of adding large number of new product pages</a><br />
				
			</h3>

			

			<div class="category-content">
				
				<p dir="auto">If I have an eCommerce website containing 10,000 product pages and then I add 10,000 new product pages using a bulk upload (with limited/basic but unique content), does this pose any SEO risk?
I am obviously aware of the risks of adding a large number of low quality content to the website, which is not the case here, however what I am trying to ascertain is whether simply doubling the number of pages in itself causes any risk to our SEO efforts? Does it flag to the Search Engines that something "spammy" is happening (even if its not)
</p>
				
				
				<small class="category-name">
					<a href="/community/q/category/16/intermediate-advanced-seo"><span class="fa-stack fa-lg" style="background-color: #fc4949; color: #FFFFFF;"><i style="color:#FFFFFF;" class="fa fa-graduation-cap fa-stack-1x"></i></span> Intermediate &amp; Advanced SEO</a> |
				</small>
				

				<small>
					
					<span class="timeago" title="2016-04-07T09:46:55.000Z"></span>
					| <a href="/community/q/user/dhs_sh">DHS_SH</a>
					
				</small>
			</div>

			
			<div class="votes" title="Votes">
				<i class="fa fa-thumbs-up"></i> <span class="human-readable-number" title="0">0</span>
			</div>
			
		</div>
	</li>
	
	<li component="category/topic" class="clearfix category-item locked unread " data-tid="55772" data-index="2" data-cid="16" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
		<link itemprop="url" content="/community/q/topic/55772/what-to-do-when-your-home-page-an-index-for-a-series-of-pages" />
		<meta itemprop="name" content="What to do when your home page an index for a series of pages." />
		<meta itemprop="itemListOrder" content="descending" />
		<meta itemprop="position" content="3" />
		<a id="2" data-index="2" component="topic/anchor"></a>

		<div class="content">
			<div class="avatar pull-left">
				

				
				<a href="/community/q/user/velocitywebsites" class="pull-left">
					
					<img class="avatar not-responsive avatar-rounded" alt="VelocityWebsites" title="VelocityWebsites" data-uid="91079" loading="lazy" component="avatar/picture" src="/community/q/assets/uploads/profile/91079-profileavatar-1619583208014.png" style="width: 46px; height: 46px; line-height: 46px; font-size: 2.875rem;" />
					
				</a>
				
			</div>

			<h3 component="topic/header" class="title">
				<i component="topic/pinned" class="fa fa-thumb-tack hide" title="Pinned"></i>
				<i component="topic/locked" class="fa fa-lock " title="Locked"></i>
				<i component="topic/moved" class="fa fa-arrow-circle-right hide" title="Moved"></i>
				

				
				<a href="/community/q/topic/55772/what-to-do-when-your-home-page-an-index-for-a-series-of-pages/9" itemprop="url">What to do when your home page an index for a series of pages.</a><br />
				
			</h3>

			

			<div class="category-content">
				
				<p dir="auto">I have created an index stack.  My home page is http://www.southernwhitewater.com
The home page is the index itself and the 1st page http://www.southernwhitewater.com/nz-adventure-tours-whitewater-river-rafting-hunting-fishing
My home page (if your look at it through moz bat for chrome bar} incorporates all the pages in the index. Is this Bad?  I would prefer to index each page separately.  As per my site index in the footer
What is the best way to optimize all these pages individually and still have the customers arrive at the top to a picture.  rel= canonical?
Any help would be great!!
http://www.southernwhitewater.com
</p>
				
				
				<small class="category-name">
					<a href="/community/q/category/16/intermediate-advanced-seo"><span class="fa-stack fa-lg" style="background-color: #fc4949; color: #FFFFFF;"><i style="color:#FFFFFF;" class="fa fa-graduation-cap fa-stack-1x"></i></span> Intermediate &amp; Advanced SEO</a> |
				</small>
				

				<small>
					
					<span class="timeago" title="2015-09-20T05:44:50.000Z"></span>
					| <a href="/community/q/user/velocitywebsites">VelocityWebsites</a>
					
				</small>
			</div>

			
			<div class="votes" title="Votes">
				<i class="fa fa-thumbs-up"></i> <span class="human-readable-number" title="0">0</span>
			</div>
			
		</div>
	</li>
	
	<li component="category/topic" class="clearfix category-item locked unread " data-tid="55351" data-index="3" data-cid="16" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
		<link itemprop="url" content="/community/q/topic/55351/i-ve-got-duplicate-pages-for-example-blog-page-2-is-the-same-as-author-admin-page-2-is-this-something-i-should-just-ignore-or-should-i-create-the-author-admin-page2-and-then-301-redirect" />
		<meta itemprop="name" content="I&#x27;ve got duplicate pages. For example, blog&#x2F;page&#x2F;2 is the same as author&#x2F;admin&#x2F;page&#x2F;2&#x5C;. Is this something I should just ignore, or should I create the author&#x2F;admin&#x2F;page2 and then 301 redirect?" />
		<meta itemprop="itemListOrder" content="descending" />
		<meta itemprop="position" content="4" />
		<a id="3" data-index="3" component="topic/anchor"></a>

		<div class="content">
			<div class="avatar pull-left">
				

				
				<a href="/community/q/user/shift-inc" class="pull-left">
					
					<img class="avatar not-responsive avatar-rounded" alt="shift-inc" title="shift-inc" data-uid="71696" loading="lazy" component="avatar/picture" src="/community/q/assets/uploads/profile/71696-profileavatar-1619583200464.png" style="width: 46px; height: 46px; line-height: 46px; font-size: 2.875rem;" />
					
				</a>
				
			</div>

			<h3 component="topic/header" class="title">
				<i component="topic/pinned" class="fa fa-thumb-tack hide" title="Pinned"></i>
				<i component="topic/locked" class="fa fa-lock " title="Locked"></i>
				<i component="topic/moved" class="fa fa-arrow-circle-right hide" title="Moved"></i>
				

				
				<a href="/community/q/topic/55351/i-ve-got-duplicate-pages-for-example-blog-page-2-is-the-same-as-author-admin-page-2-is-this-something-i-should-just-ignore-or-should-i-create-the-author-admin-page2-and-then-301-redirect/7" itemprop="url">I&#x27;ve got duplicate pages. For example, blog&#x2F;page&#x2F;2 is the same as author&#x2F;admin&#x2F;page&#x2F;2&#x5C;. Is this something I should just ignore, or should I create the author&#x2F;admin&#x2F;page2 and then 301 redirect?</a><br />
				
			</h3>

			

			<div class="category-content">
				
				<p dir="auto">I'm going through the crawl report and it says I've got duplicate pages. For example, blog/page/2 is the same as   author/admin/page/2/  Now, the author/admin/page/2 I can't even find in WordPress, but it is the same thing as blog/page/2 nonetheless. Is this something I should just ignore, or should I create the author/admin/page2 and then 301 redirect it to blog/page/2?
</p>
				
				
				<small class="category-name">
					<a href="/community/q/category/16/intermediate-advanced-seo"><span class="fa-stack fa-lg" style="background-color: #fc4949; color: #FFFFFF;"><i style="color:#FFFFFF;" class="fa fa-graduation-cap fa-stack-1x"></i></span> Intermediate &amp; Advanced SEO</a> |
				</small>
				

				<small>
					
					<span class="timeago" title="2015-08-21T14:28:04.000Z"></span>
					| <a href="/community/q/user/shift-inc">shift-inc</a>
					
				</small>
			</div>

			
			<div class="votes" title="Votes">
				<i class="fa fa-thumbs-up"></i> <span class="human-readable-number" title="0">0</span>
			</div>
			
		</div>
	</li>
	
	<li component="category/topic" class="clearfix category-item locked unread " data-tid="54568" data-index="4" data-cid="16" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
		<link itemprop="url" content="/community/q/topic/54568/on-1-of-our-sites-we-have-our-company-name-in-the-h1-on-our-other-site-we-have-the-page-title-in-our-h1-does-anyone-have-any-advise-about-the-best-information-to-have-in-the-h1-h2-and-page-tile" />
		<meta itemprop="name" content="On 1 of our sites we have our Company name in the H1 on our other site we have the page title in our H1 - does anyone have any advise about the best information to have in the H1, H2 and Page Tile" />
		<meta itemprop="itemListOrder" content="descending" />
		<meta itemprop="position" content="5" />
		<a id="4" data-index="4" component="topic/anchor"></a>

		<div class="content">
			<div class="avatar pull-left">
				

				
				<a href="/community/q/user/costumed" class="pull-left">
					
					<img class="avatar not-responsive avatar-rounded" alt="CostumeD" title="CostumeD" data-uid="83039" loading="lazy" component="avatar/icon" src="https://moz.com/avatar/large/9/c.png"></img>
					
				</a>
				
			</div>

			<h3 component="topic/header" class="title">
				<i component="topic/pinned" class="fa fa-thumb-tack hide" title="Pinned"></i>
				<i component="topic/locked" class="fa fa-lock " title="Locked"></i>
				<i component="topic/moved" class="fa fa-arrow-circle-right hide" title="Moved"></i>
				

				
				<a href="/community/q/topic/54568/on-1-of-our-sites-we-have-our-company-name-in-the-h1-on-our-other-site-we-have-the-page-title-in-our-h1-does-anyone-have-any-advise-about-the-best-information-to-have-in-the-h1-h2-and-page-tile/7" itemprop="url">On 1 of our sites we have our Company name in the H1 on our other site we have the page title in our H1 - does anyone have any advise about the best information to have in the H1, H2 and Page Tile</a><br />
				
			</h3>

			

			<div class="category-content">
				
				<p dir="auto">We have 2 sites that have been set up slightly differently. On 1 site we have the Company name in the H1 and the product name in the page title and H2. On the other site we have the Product name in the H1 and no H2.
Does anyone have any advise about the best information to have in the H1 and H2
</p>
				
				
				<small class="category-name">
					<a href="/community/q/category/16/intermediate-advanced-seo"><span class="fa-stack fa-lg" style="background-color: #fc4949; color: #FFFFFF;"><i style="color:#FFFFFF;" class="fa fa-graduation-cap fa-stack-1x"></i></span> Intermediate &amp; Advanced SEO</a> |
				</small>
				

				<small>
					
					<span class="timeago" title="2015-07-08T10:13:17.000Z"></span>
					| <a href="/community/q/user/costumed">CostumeD</a>
					
				</small>
			</div>

			
			<div class="votes" title="Votes">
				<i class="fa fa-thumbs-up"></i> <span class="human-readable-number" title="0">0</span>
			</div>
			
		</div>
	</li>
	
	<li component="category/topic" class="clearfix category-item locked unread " data-tid="38135" data-index="5" data-cid="16" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
		<link itemprop="url" content="/community/q/topic/38135/varying-internal-link-anchor-text-with-each-new-page-load" />
		<meta itemprop="name" content="Varying Internal Link Anchor Text with Each New Page Load" />
		<meta itemprop="itemListOrder" content="descending" />
		<meta itemprop="position" content="6" />
		<a id="5" data-index="5" component="topic/anchor"></a>

		<div class="content">
			<div class="avatar pull-left">
				

				
				<a href="/community/q/user/ryanod" class="pull-left">
					
					<img class="avatar not-responsive avatar-rounded" alt="RyanOD" title="RyanOD" data-uid="5203" loading="lazy" component="avatar/icon" src="https://moz.com/avatar/large/3/r.png"></img>
					
				</a>
				
			</div>

			<h3 component="topic/header" class="title">
				<i component="topic/pinned" class="fa fa-thumb-tack hide" title="Pinned"></i>
				<i component="topic/locked" class="fa fa-lock " title="Locked"></i>
				<i component="topic/moved" class="fa fa-arrow-circle-right hide" title="Moved"></i>
				

				
				<a href="/community/q/topic/38135/varying-internal-link-anchor-text-with-each-new-page-load/7" itemprop="url">Varying Internal Link Anchor Text with Each New Page Load</a><br />
				
			</h3>

			

			<div class="category-content">
				
				<p dir="auto">I'm asking for people's opinions on varying internal anchor text. Before you jump in and say, "Oh yes, varying your anchor text is always a good idea", let me explain.
I'm not talking about varying anchor text on different links scattered throughout a site. We all know that is a wise thing to do for a variety of reasons that have been covered in many places. What I'm talking about is including semi-useful links below the fold and then varying the anchor text with each page load. Each time Googlebot crawls a page, it sees different anchor text for each link. That way, Googlebot is seeing, for example, 'san diego bars', 'taverns in san diego', 'san diego clubs', and 'pubs in san diego' all pointing to a San Diego bar/tavern/club/pub page.
I'm wondering if there is value in this approach. Will it help a site rank well for multiple search queries? Could it potentially be better than static anchor text as it may help Google better understand the targeted page? Is it a good way to protect a large site with a huge number of internal links from Penguin?
To summarize, we're talking about the impact of varying the anchor text on a single page with each page load as opposed to varying the anchor text on different pages.
Thoughts?
</p>
				
				
				<small class="category-name">
					<a href="/community/q/category/16/intermediate-advanced-seo"><span class="fa-stack fa-lg" style="background-color: #fc4949; color: #FFFFFF;"><i style="color:#FFFFFF;" class="fa fa-graduation-cap fa-stack-1x"></i></span> Intermediate &amp; Advanced SEO</a> |
				</small>
				

				<small>
					
					<span class="timeago" title="2013-07-22T04:08:45.000Z"></span>
					| <a href="/community/q/user/ryanod">RyanOD</a>
					
				</small>
			</div>

			
			<div class="votes" title="Votes">
				<i class="fa fa-thumbs-up"></i> <span class="human-readable-number" title="0">0</span>
			</div>
			
		</div>
	</li>
	
	<li component="category/topic" class="clearfix category-item locked unread " data-tid="19725" data-index="6" data-cid="16" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
		<link itemprop="url" content="/community/q/topic/19725/landing-page-home-page-redesign-seo-factor-question-serious-concern" />
		<meta itemprop="name" content="Landing Page - Home Page redesign SEO factor question - Serious concern." />
		<meta itemprop="itemListOrder" content="descending" />
		<meta itemprop="position" content="7" />
		<a id="6" data-index="6" component="topic/anchor"></a>

		<div class="content">
			<div class="avatar pull-left">
				

				
				<a href="/community/q/user/meninkilts" class="pull-left">
					
					<img class="avatar not-responsive avatar-rounded" alt="MenInKilts" title="MenInKilts" data-uid="36591" loading="lazy" component="avatar/picture" src="/community/q/assets/uploads/profile/36591-profileavatar-1619579317274.png" style="width: 46px; height: 46px; line-height: 46px; font-size: 2.875rem;" />
					
				</a>
				
			</div>

			<h3 component="topic/header" class="title">
				<i component="topic/pinned" class="fa fa-thumb-tack hide" title="Pinned"></i>
				<i component="topic/locked" class="fa fa-lock " title="Locked"></i>
				<i component="topic/moved" class="fa fa-arrow-circle-right hide" title="Moved"></i>
				

				
				<a href="/community/q/topic/19725/landing-page-home-page-redesign-seo-factor-question-serious-concern/8" itemprop="url">Landing Page - Home Page redesign SEO factor question - Serious concern.</a><br />
				
			</h3>

			

			<div class="category-content">
				
				<p dir="auto">Hi Folks,
I'm considering making a big change to our website and really need some expert advise. Will we lose ranking if we do what I propose?
Our site www.meninkilts.com, needs to split users/clients by "Commercial" and "Residential" so we can message/market completely differently to each client.
We are considering doing this structure:
Landing Page
|
|
Commercial Homepage  Residential Homepage
Right now we rank well, for our keywords like "Window Cleaning cityname" but are worried that adding a landing page, and splitting our site to two homepages will effect seo (ie: a landing page would only have two buttons: one for commercial and one for residential).
What would be the best way to handle this. Looking forward to your insights!
Cheers Brent
</p>
				
				
				<small class="category-name">
					<a href="/community/q/category/16/intermediate-advanced-seo"><span class="fa-stack fa-lg" style="background-color: #fc4949; color: #FFFFFF;"><i style="color:#FFFFFF;" class="fa fa-graduation-cap fa-stack-1x"></i></span> Intermediate &amp; Advanced SEO</a> |
				</small>
				

				<small>
					
					<span class="timeago" title="2012-06-07T13:12:36.000Z"></span>
					| <a href="/community/q/user/meninkilts">MenInKilts</a>
					
				</small>
			</div>

			
			<div class="votes" title="Votes">
				<i class="fa fa-thumbs-up"></i> <span class="human-readable-number" title="0">0</span>
			</div>
			
		</div>
	</li>
	
	<li component="category/topic" class="clearfix category-item locked unread " data-tid="8784" data-index="7" data-cid="16" itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
		<link itemprop="url" content="/community/q/topic/8784/does-a-page-on-a-site-with-high-domain-authority-build-page-authority-easier-i-e-less-inbound-links" />
		<meta itemprop="name" content="Does a page on a site with high domain authority build page authority easier? i.e. less inbound links?" />
		<meta itemprop="itemListOrder" content="descending" />
		<meta itemprop="position" content="8" />
		<a id="7" data-index="7" component="topic/anchor"></a>

		<div class="content">
			<div class="avatar pull-left">
				

				
				<a href="/community/q/user/adriandg" class="pull-left">
					
					<img class="avatar not-responsive avatar-rounded" alt="adriandg" title="adriandg" data-uid="20721" loading="lazy" component="avatar/picture" src="https://moz.com/avatar/user/264819" style="width: 46px; height: 46px; line-height: 46px; font-size: 2.875rem;" />
					
				</a>
				
			</div>

			<h3 component="topic/header" class="title">
				<i component="topic/pinned" class="fa fa-thumb-tack hide" title="Pinned"></i>
				<i component="topic/locked" class="fa fa-lock " title="Locked"></i>
				<i component="topic/moved" class="fa fa-arrow-circle-right hide" title="Moved"></i>
				

				
				<a href="/community/q/topic/8784/does-a-page-on-a-site-with-high-domain-authority-build-page-authority-easier-i-e-less-inbound-links/6" itemprop="url">Does a page on a site with high domain authority build page authority easier? i.e. less inbound links?</a><br />
				
			</h3>

			

			<div class="category-content">
				
				<p dir="auto">Is this also why people build backlinks to their BBB profiles, Yellowpages Profiles, etc. i.e. why do people build backlinks to other pages that link to them?  Wouldn't it be more beneficial to just build that backlink directly to your target?
</p>
				
				
				<small class="category-name">
					<a href="/community/q/category/16/intermediate-advanced-seo"><span class="fa-stack fa-lg" style="background-color: #fc4949; color: #FFFFFF;"><i style="color:#FFFFFF;" class="fa fa-graduation-cap fa-stack-1x"></i></span> Intermediate &amp; Advanced SEO</a> |
				</small>
				

				<small>
					
					<span class="timeago" title="2011-10-04T15:30:53.000Z"></span>
					| <a href="/community/q/user/adriandg">adriandg</a>
					
				</small>
			</div>

			
			<div class="votes" title="Votes">
				<i class="fa fa-thumbs-up"></i> <span class="human-readable-number" title="0">0</span>
			</div>
			
		</div>
	</li>
	
</ul>

	</div>
</div>

		
	</div>
</div>

<div data-widget-area="footer">
	
</div>


<script id="ajaxify-data" type="application/json">{"cid":16,"lastposttime":1455698895000,"mainPid":58032,"postcount":3,"slug":"58032/pages-with-excessive-number-of-links","tid":58032,"timestamp":1455693059000,"title":"Pages with excessive number of links","uid":101325,"viewcount":1925,"__imported_original_data__":"{\"_tid\":86869,\"_uid\":4474357,\"_cid\":8,\"_private\":0,\"_title\":\"Pages with excessive number of links\",\"_content\":\"<p>Hi all, I work for a retailer and I've crawled our website with RankTracker for optimization suggestions.<\/p>\\r\\n<p>The main suggestion is \\\"Pages with excessive number of links: 4178\\\"<\/p>\\r\\n<p>The page with the largest amount of links has 634 links (627 internal, 7 external), the lowest 382 links (375 internal, 7 external).<\/p>\\r\\n<p>However, when I view the source on any one of the example pages, it becomes obvious that the site's main navigation header contains 358 links, so every new page starts with 358 links before any content.<br /><br />Our rivals and much larger sites like argos.co.uk appear to have just as many links in their main navigation menu.<\/p>\\r\\n<p>So my questions are:<\/p>\\r\\n<p>1. Will these excessive links really be causing us a problem or is it just 'good practice' to have fewer links<br />2. Can I use 'no follow' to stop Google etc from counting the 358 main navigation links<br />3. Is have 4000+ pages of your website all dumbly pointing to other pages a help or hindrance?<br />4. Can we 'minify' this code so it's cached on first load and therefore loads faster?<\/p>\\r\\n<p>Thank you.<\/p>\",\"_timestamp\":1455693059000,\"_viewcount\":1404,\"_locked\":0,\"_pinned\":0,\"_answered\":1,\"_note\":null,\"_status\":null,\"_assignedToId\":null,\"_slug\":\"pages-with-excessive-number-of-links\",\"_attachments\":[],\"_flags\":[],\"_spam\":0,\"_inappropriate\":0,\"_incorrect\":0,\"_deleted\":0,\"imported\":true}","teaserPid":288602,"postercount":3,"locked":1,"deleted":0,"pinned":0,"pinExpiry":0,"upvotes":0,"downvotes":0,"deleterUid":0,"titleRaw":"Pages with excessive number of links","timestampISO":"2016-02-17T07:10:59.000Z","scheduled":false,"lastposttimeISO":"2016-02-17T08:48:15.000Z","pinExpiryISO":"","votes":0,"tags":[],"thumbs":[],"posts":[{"content":"<p dir=\"auto\">Hi all, I work for a retailer and I've crawled our website with RankTracker for optimization suggestions.<\/p>\n<p dir=\"auto\">The main suggestion is \"Pages with excessive number of links: 4178\"<\/p>\n<p dir=\"auto\">The page with the largest amount of links has 634 links (627 internal, 7 external), the lowest 382 links (375 internal, 7 external).<\/p>\n<p dir=\"auto\">However, when I view the source on any one of the example pages, it becomes obvious that the site's main navigation header contains 358 links, so every new page starts with 358 links before any content.<\/p>\n<p dir=\"auto\">Our rivals and much larger sites like <a href=\"http://argos.co.uk\" rel=\"nofollow ugc\">argos.co.uk<\/a> appear to have just as many links in their main navigation menu.<\/p>\n<p dir=\"auto\">So my questions are:<\/p>\n<p dir=\"auto\">1. Will these excessive links really be causing us a problem or is it just 'good practice' to have fewer links<br />\n2. Can I use 'no follow' to stop Google etc from counting the 358 main navigation links<br />\n3. Is have 4000+ pages of your website all dumbly pointing to other pages a help or hindrance?<br />\n4. Can we 'minify' this code so it's cached on first load and therefore loads faster?<\/p>\n<p dir=\"auto\">Thank you.<\/p>\n","pid":58032,"tid":58032,"timestamp":1455693059000,"uid":101325,"reputation":0,"votes":0,"deleted":0,"upvotes":0,"downvotes":0,"deleterUid":0,"edited":0,"replies":{"hasMore":false,"users":[],"text":"[[topic:one_reply_to_this_post]]","count":0},"bookmarks":0,"timestampISO":"2016-02-17T07:10:59.000Z","editedISO":"","index":0,"eventStart":1455698895000,"eventEnd":1728956660847,"user":{"uid":101325,"username":"Bee159","userslug":"bee159","reputation":7,"postcount":43,"topiccount":27,"picture":"/community/q/assets/uploads/profile/101325-profileavatar-1619582721754.png","signature":"","banned":false,"banned:expire":0,"status":"offline","lastonline":1507625518000,"groupTitle":null,"mutedUntil":0,"displayname":"Bee159","groupTitleArray":[],"icon:text":"B","icon:bgColor":"#1b5e20","lastonlineISO":"2017-10-10T08:51:58.000Z","banned_until":0,"banned_until_readable":"Not Banned","muted":false,"selectedGroups":[],"custom_profile_info":[],"mozId":null},"editor":null,"bookmarked":false,"upvoted":false,"downvoted":false,"selfPost":false,"topicOwnerPost":true,"display_edit_tools":false,"display_delete_tools":false,"display_moderator_tools":false,"display_move_tools":false,"display_post_menu":true},{"content":"<p dir=\"auto\">There has even been a Google Webmaster Guidelines Update in February 2016 which states<\/p>\n<p dir=\"auto\">\"Limit the number of links on a page to a reasonable number <strong>(a few thousand at most<\/strong>).\"  (Source: <a href=\"https://support.google.com/webmasters/answer/35769?hl=en\" rel=\"nofollow ugc\">https://support.google.com/webmasters/answer/35769?hl=en<\/a>)<\/p>\n<p dir=\"auto\">So I really would not bother too much, especially not in a navigation - it often makes lots of sense to have lots of links there. (For example I have several alphabetical selections available on hover from main categories. It would not make sense to remove them just to have fewer links.)<\/p>\n<p dir=\"auto\">More links are of course not always better - consider what the user is likely to expect/need in navigation etc. Of course, more links mean that the relative importance of each link decreases; but google is able to identify navigation and repeating elements that appear on every page. I'd assume that they treat them different to main-content links. Because, well, they feel a lot different.<\/p>\n<p dir=\"auto\">Regards<\/p>\n<p dir=\"auto\">Nico<\/p>\n","pid":288602,"tid":58032,"timestamp":1455698895000,"uid":35115,"__imported_original_data__":"{\"_pid\":331119,\"_tid\":86869,\"_uid\":380439,\"_content\":\"<p>There has even been a Google Webmaster Guidelines Update in February 2016 which states<\/p>\\r\\n<p>\\\"Limit the number of links on a page to a reasonable number <strong>(a few thousand at most<\/strong>).\\\"&nbsp; (Source: https://support.google.com/webmasters/answer/35769?hl=en)<\/p>\\r\\n<p>So I really would not bother too much, especially not in a navigation - it often makes lots of sense to have lots of links there. (For example I have several alphabetical selections available on hover from main categories. It would not make sense to remove them just to have fewer links.)<\/p>\\r\\n<p>More links are of course not always better - consider what the user is likely to expect/need in navigation etc. Of course, more links mean that the relative importance of each link decreases; but google is able to identify navigation and repeating elements that appear on every page. I'd assume that they treat them different to main-content links. Because, well, they feel a lot different.<\/p>\\r\\n<p>Regards<\/p>\\r\\n<p>Nico<\/p>\",\"_deletedAt\":null,\"_edited\":1455722190000,\"_toTpid\":86869,\"_toType\":\"Question\",\"_tslug\":\"pages-with-excessive-number-of-links\",\"_timestamp\":1455698895000,\"_attachments\":[],\"_flags\":[],\"_spam\":0,\"_inappropriate\":0,\"_incorrect\":0,\"_deleted\":0}","edited":1455722190000,"reputation":0,"votes":1,"downvotes":0,"upvotes":1,"deleted":0,"deleterUid":0,"replies":{"hasMore":false,"users":[],"text":"[[topic:one_reply_to_this_post]]","count":0},"bookmarks":0,"timestampISO":"2016-02-17T08:48:15.000Z","editedISO":"2016-02-17T15:16:30.000Z","index":1,"eventStart":1455697844000,"eventEnd":1455698895000,"user":{"uid":35115,"username":"netzkern_AG","userslug":"netzkern_ag","reputation":33,"postcount":54,"topiccount":15,"picture":null,"signature":"","banned":false,"banned:expire":0,"status":"offline","lastonline":1627387099701,"groupTitle":"[\"qa_subscriber\"]","mutedUntil":0,"displayname":"netzkern_AG","groupTitleArray":["qa_subscriber"],"icon:text":"N","icon:bgColor":"#009688","lastonlineISO":"2021-07-27T11:58:19.701Z","banned_until":0,"banned_until_readable":"Not Banned","muted":false,"selectedGroups":[{"name":"qa_subscriber","slug":"qa_subscriber","labelColor":"#4dbdeb","textColor":"#ffffff","icon":"fa-check-circle","userTitle":"Subscriber"}],"custom_profile_info":[],"mozId":380439},"editor":null,"bookmarked":false,"upvoted":false,"downvoted":false,"selfPost":false,"topicOwnerPost":false,"display_edit_tools":false,"display_delete_tools":false,"display_moderator_tools":false,"display_move_tools":false,"display_post_menu":true},{"content":"<p dir=\"auto\">Pre 2013 it was bad practice to have in excess of 100 links per page, google technical guideline.  Many SEO tools still use it as a warning bell. However Matt Cutts from google - I recall a few years ago - came out and categorically said it is NOT bad practice.  Have as many links as you like as long as it is natural and helps the customer.<\/p>\n<p dir=\"auto\">What Matt did say is if it appears like spam, them google will penalize you accordingly. Here we go just found the video. <a href=\"https://www.youtube.com/watch?v=QHG6BkmzDEM\" rel=\"nofollow ugc\">https://www.youtube.com/watch?v=QHG6BkmzDEM<\/a><\/p>\n<p dir=\"auto\">So to be clear - if the links are needed and help the customer - I would not concern myself.  Watch the video, nothing better than going straight to the source.<\/p>\n<p dir=\"auto\">Hope that assists<\/p>\n","pid":288601,"tid":58032,"timestamp":1455697844000,"uid":77292,"__imported_original_data__":"{\"_pid\":331117,\"_tid\":86869,\"_uid\":3938129,\"_content\":\"<p>Pre 2013 it was bad practice to have in excess of 100 links per page, google technical guideline. &nbsp;Many SEO tools still use it as a warning bell. However Matt Cutts from google - I recall a few years ago - came out and categorically said it is NOT bad practice. &nbsp;Have as many links as you like as long as it is natural and helps the customer. &nbsp;<\/p>\\r\\n<p>What Matt did say is if it appears like spam, them google will penalize you accordingly. Here we go just found the video.&nbsp;https://www.youtube.com/watch?v=QHG6BkmzDEM<\/p>\\r\\n<p>So to be clear - if the links are needed and help the customer - I would not concern myself. &nbsp;Watch the video, nothing better than going straight to the source.<\/p>\\r\\n<p>Hope that assists&nbsp;<\/p>\",\"_deletedAt\":null,\"_edited\":1455698582000,\"_toTpid\":86869,\"_toType\":\"Question\",\"_tslug\":\"pages-with-excessive-number-of-links\",\"_timestamp\":1455697844000,\"_attachments\":[],\"_flags\":[],\"_spam\":0,\"_inappropriate\":0,\"_incorrect\":0,\"_deleted\":0}","edited":1455698582000,"reputation":0,"votes":1,"downvotes":0,"upvotes":1,"deleted":0,"deleterUid":0,"replies":{"hasMore":false,"users":[],"text":"[[topic:one_reply_to_this_post]]","count":0},"bookmarks":0,"timestampISO":"2016-02-17T08:30:44.000Z","editedISO":"2016-02-17T08:43:02.000Z","index":2,"eventStart":1455693059000,"eventEnd":1455697844000,"user":{"uid":77292,"username":"ClaytonJ","userslug":"claytonj","reputation":576,"postcount":562,"topiccount":2,"picture":"/community/q/assets/uploads/profile/77292-profileavatar-1619582671334.png","signature":"","banned":false,"banned:expire":0,"status":"offline","lastonline":1601036633000,"groupTitle":"[\"qa_indexed_profiles\"]","mutedUntil":0,"displayname":"ClaytonJ","groupTitleArray":["qa_indexed_profiles"],"icon:text":"C","icon:bgColor":"#009688","lastonlineISO":"2020-09-25T12:23:53.000Z","banned_until":0,"banned_until_readable":"Not Banned","muted":false,"selectedGroups":[],"custom_profile_info":[],"mozId":null},"editor":null,"bookmarked":false,"upvoted":false,"downvoted":false,"selfPost":false,"topicOwnerPost":false,"display_edit_tools":false,"display_delete_tools":false,"display_moderator_tools":false,"display_move_tools":false,"display_post_menu":true}],"events":[{"type":"lock","uid":"212392","id":239084,"timestamp":1720626050250,"timestampISO":"2024-07-10T15:40:50.250Z","user":{"picture":null,"username":"Kristin_Fast","userslug":"kristin_fast","uid":212392,"displayname":"Kristin_Fast","icon:text":"K","icon:bgColor":"#e91e63"},"icon":"fa-lock","text":"[[topic:locked-by]]"},{"type":"lock","uid":"212392","id":233161,"timestamp":1720625994714,"timestampISO":"2024-07-10T15:39:54.714Z","user":{"picture":null,"username":"Kristin_Fast","userslug":"kristin_fast","uid":212392,"displayname":"Kristin_Fast","icon:text":"K","icon:bgColor":"#e91e63"},"icon":"fa-lock","text":"[[topic:locked-by]]"},{"type":"lock","uid":"212392","id":119039,"timestamp":1720540115499,"timestampISO":"2024-07-09T15:48:35.499Z","user":{"picture":null,"username":"Kristin_Fast","userslug":"kristin_fast","uid":212392,"displayname":"Kristin_Fast","icon:text":"K","icon:bgColor":"#e91e63"},"icon":"fa-lock","text":"[[topic:locked-by]]"},{"type":"lock","uid":20417,"id":51674,"timestamp":1621008862300,"timestampISO":"2021-05-14T16:14:22.300Z","user":{"picture":"/community/q/assets/uploads/profile/20417-profileavatar-1619582455057.png","username":"ShellyMoz","userslug":"shellymoz","uid":20417,"displayname":"Shelly Matsudaira","icon:text":"S","icon:bgColor":"#ff5722"},"icon":"fa-lock","text":"[[topic:locked-by]]"}],"category":{"bgColor":"#fc4949","cid":16,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Looking to level up your SEO techniques? Chat through more advanced approaches.","descriptionParsed":"<p dir=\"auto\">Looking to level up your SEO techniques? Chat through more advanced approaches.<\/p>\n","disabled":0,"icon":"fa-graduation-cap","imageClass":"cover","isSection":0,"link":"","name":"Intermediate &amp; Advanced SEO","numRecentReplies":1,"order":8,"parentCid":9,"post_count":51901,"slug":"16/intermediate-advanced-seo","topic_count":11073,"__imported_original_data__":"{\"_cid\":8,\"_name\":\"Intermediate & Advanced SEO\",\"_parentCid\":2000,\"_timestamp\":1296250949000,\"_slug\":\"intermediate-advanced-seo\",\"_order\":7,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":51901,"totalTopicCount":11073},"tagWhitelist":[],"minTags":1,"maxTags":5,"thread_tools":[{"class":"toggleQuestionStatus alert-warning","title":"[[qanda:thread.tool.as_question]]","icon":"fa-question-circle"}],"isFollowing":false,"isNotFollowing":true,"isIgnoring":false,"bookmark":null,"postSharing":[{"id":"facebook","name":"Facebook","class":"fa-facebook","activated":true},{"id":"twitter","name":"Twitter","class":"fa-twitter","activated":true}],"deleter":null,"merger":null,"related":[],"unreplied":false,"icons":[],"privileges":{"topics:reply":false,"topics:read":true,"topics:schedule":false,"topics:tag":false,"topics:delete":false,"posts:edit":false,"posts:history":false,"posts:delete":false,"posts:view_deleted":false,"read":true,"purge":false,"view_thread_tools":false,"editable":false,"deletable":false,"view_deleted":false,"view_scheduled":false,"isAdminOrMod":false,"disabled":0,"tid":"58032","uid":0},"topicStaleDays":120,"reputation:disabled":0,"downvote:disabled":1,"feeds:disableRSS":1,"bookmarkThreshold":5,"necroThreshold":7,"postEditDuration":0,"postDeleteDuration":0,"scrollToMyPost":true,"updateUrlWithPostIndex":true,"allowMultipleBadges":true,"privateUploads":false,"showPostPreviewsOnHover":true,"rssFeedUrl":"/community/q/topic/58032.rss","postIndex":3,"breadcrumbs":[{"text":"[[global:home]]","url":"/community/q/"},{"text":"SEO Tactics","url":"/community/q/category/9/seo-tactics","cid":9},{"text":"Intermediate &amp; Advanced SEO","url":"/community/q/category/16/intermediate-advanced-seo","cid":16},{"text":"Pages with excessive number of links"}],"pagination":{"prev":{"page":1,"active":false},"next":{"page":1,"active":false},"first":{"page":1,"active":true},"last":{"page":1,"active":true},"rel":[],"pages":[],"currentPage":1,"pageCount":1},"loggedIn":false,"relative_path":"/community/q","template":{"name":"topic","topic":true},"url":"/community/q/topic/58032/pages-with-excessive-number-of-links/3","bodyClass":"page-topic page-topic-58032 page-topic-pages-with-excessive-number-of-links page-topic-category-16 page-topic-category-intermediate-amp-advanced-seo parent-category-9 parent-category-16 page-status-200 theme-moz user-guest","mainPost":{"content":"<p dir=\\\"auto\\\">Hi all, I work for a retailer and I've crawled our website with RankTracker for optimization suggestions.<\/p>\n<p dir=\\\"auto\\\">The main suggestion is \\\"Pages with excessive number of links: 4178\\\"<\/p>\n<p dir=\\\"auto\\\">The page with the largest amount of links has 634 links (627 internal, 7 external), the lowest 382 links (375 internal, 7 external).<\/p>\n<p dir=\\\"auto\\\">However, when I view the source on any one of the example pages, it becomes obvious that the site's main navigation header contains 358 links, so every new page starts with 358 links before any content.<\/p>\n<p dir=\\\"auto\\\">Our rivals and much larger sites like <a href=\\\"http://argos.co.uk\\\" rel=\\\"nofollow ugc\\\">argos.co.uk<\/a> appear to have just as many links in their main navigation menu.<\/p>\n<p dir=\\\"auto\\\">So my questions are:<\/p>\n<p dir=\\\"auto\\\">1. Will these excessive links really be causing us a problem or is it just 'good practice' to have fewer links<br />\n2. Can I use 'no follow' to stop Google etc from counting the 358 main navigation links<br />\n3. Is have 4000+ pages of your website all dumbly pointing to other pages a help or hindrance?<br />\n4. Can we 'minify' this code so it's cached on first load and therefore loads faster?<\/p>\n<p dir=\\\"auto\\\">Thank you.<\/p>\n","pid":58032,"tid":58032,"timestamp":1455693059000,"uid":101325,"reputation":0,"votes":0,"deleted":0,"upvotes":0,"downvotes":0,"deleterUid":0,"edited":0,"replies":{"hasMore":false,"users":[],"text":"[[topic:one_reply_to_this_post]]","count":0},"bookmarks":0,"timestampISO":"2016-02-17T07:10:59.000Z","editedISO":"","user":{"uid":101325,"username":"Bee159","userslug":"bee159","reputation":7,"postcount":43,"topiccount":27,"picture":"/community/q/assets/uploads/profile/101325-profileavatar-1619582721754.png","signature":"","banned":false,"banned:expire":0,"status":"offline","lastonline":1507625518000,"groupTitle":null,"mutedUntil":0,"displayname":"Bee159","groupTitleArray":[],"icon:text":"B","icon:bgColor":"#1b5e20","lastonlineISO":"2017-10-10T08:51:58.000Z","banned_until":0,"banned_until_readable":"Not Banned","muted":false,"selectedGroups":[],"custom_profile_info":[],"mozId":null},"editor":null,"bookmarked":false,"upvoted":false,"downvoted":false,"selfPost":false},"suggestedAnswer":{"content":"<p dir=\\\"auto\\\">Pre 2013 it was bad practice to have in excess of 100 links per page, google technical guideline.  Many SEO tools still use it as a warning bell. However Matt Cutts from google - I recall a few years ago - came out and categorically said it is NOT bad practice.  Have as many links as you like as long as it is natural and helps the customer.<\/p>\n<p dir=\\\"auto\\\">What Matt did say is if it appears like spam, them google will penalize you accordingly. Here we go just found the video. <a href=\\\"https://www.youtube.com/watch?v=QHG6BkmzDEM\\\" rel=\\\"nofollow ugc\\\">https://www.youtube.com/watch?v=QHG6BkmzDEM<\/a><\/p>\n<p dir=\\\"auto\\\">So to be clear - if the links are needed and help the customer - I would not concern myself.  Watch the video, nothing better than going straight to the source.<\/p>\n<p dir=\\\"auto\\\">Hope that assists<\/p>\n","pid":288601,"tid":58032,"timestamp":1455697844000,"uid":77292,"__imported_original_data__":"{\"_pid\":331117,\"_tid\":86869,\"_uid\":3938129,\"_content\":\"<p>Pre 2013 it was bad practice to have in excess of 100 links per page, google technical guideline. &nbsp;Many SEO tools still use it as a warning bell. However Matt Cutts from google - I recall a few years ago - came out and categorically said it is NOT bad practice. &nbsp;Have as many links as you like as long as it is natural and helps the customer. &nbsp;<\/p>\\r\\n<p>What Matt did say is if it appears like spam, them google will penalize you accordingly. Here we go just found the video.&nbsp;https://www.youtube.com/watch?v=QHG6BkmzDEM<\/p>\\r\\n<p>So to be clear - if the links are needed and help the customer - I would not concern myself. &nbsp;Watch the video, nothing better than going straight to the source.<\/p>\\r\\n<p>Hope that assists&nbsp;<\/p>\",\"_deletedAt\":null,\"_edited\":1455698582000,\"_toTpid\":86869,\"_toType\":\"Question\",\"_tslug\":\"pages-with-excessive-number-of-links\",\"_timestamp\":1455697844000,\"_attachments\":[],\"_flags\":[],\"_spam\":0,\"_inappropriate\":0,\"_incorrect\":0,\"_deleted\":0}","edited":1455698582000,"reputation":0,"votes":1,"downvotes":0,"upvotes":1,"deleted":0,"deleterUid":0,"replies":{"hasMore":false,"users":[],"text":"[[topic:one_reply_to_this_post]]","count":0},"bookmarks":0,"timestampISO":"2016-02-17T08:30:44.000Z","editedISO":"2016-02-17T08:43:02.000Z","user":{"uid":77292,"username":"ClaytonJ","userslug":"claytonj","reputation":576,"postcount":562,"topiccount":2,"picture":"/community/q/assets/uploads/profile/77292-profileavatar-1619582671334.png","signature":"","banned":false,"banned:expire":0,"status":"offline","lastonline":1601036633000,"groupTitle":"[\"qa_indexed_profiles\"]","mutedUntil":0,"displayname":"ClaytonJ","groupTitleArray":["qa_indexed_profiles"],"icon:text":"C","icon:bgColor":"#009688","lastonlineISO":"2020-09-25T12:23:53.000Z","banned_until":0,"banned_until_readable":"Not Banned","muted":false,"selectedGroups":[],"custom_profile_info":[],"mozId":null},"editor":null,"bookmarked":false,"upvoted":false,"downvoted":false,"selfPost":false},"acceptedAnswer":{},"answerCount":2,"categoryList":[{"bgColor":"#4dbdeb","cid":47,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Chat with the community about the Moz tools.","descriptionParsed":"<p dir=\"auto\">Chat with the community about the Moz tools.<\/p>\n","disabled":0,"icon":"fa-wrench","imageClass":"cover","isSection":0,"link":"","name":"Moz Tools","numRecentReplies":1,"order":1,"parentCid":0,"post_count":4100,"slug":"47/moz-tools","topic_count":48,"__imported_original_data__":"{\"_cid\":45,\"_name\":\"Moz Tools\",\"_parentCid\":1000,\"_timestamp\":1296250950000,\"_slug\":\"moz-tools\",\"_order\":1,\"_description\":\"\"}","subCategoriesPerPage":15,"postQueue":0,"minTags":1,"maxTags":5,"totalPostCount":32405,"totalTopicCount":6590,"children":[{"bgColor":"#5dc93a","cid":53,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Get up and running with the Moz tools.","descriptionParsed":"<p dir=\"auto\">Get up and running with the Moz tools.<\/p>\n","disabled":0,"icon":"fa-sort-alpha-asc","imageClass":"cover","isSection":0,"link":"","name":"Getting Started","numRecentReplies":1,"order":1,"parentCid":47,"post_count":2288,"slug":"53/getting-started","topic_count":567,"__imported_original_data__":"{\"_cid\":61,\"_name\":\"Getting Started\",\"_parentCid\":1000,\"_timestamp\":1377175562000,\"_slug\":\"getting-started\",\"_order\":2,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":2288,"totalTopicCount":567,"children":[],"parent":{"bgColor":"#4dbdeb","cid":47,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Chat with the community about the Moz tools.","descriptionParsed":"<p dir=\"auto\">Chat with the community about the Moz tools.<\/p>\n","disabled":0,"icon":"fa-wrench","imageClass":"cover","isSection":0,"link":"","name":"Moz Tools","numRecentReplies":1,"order":1,"parentCid":0,"post_count":4100,"slug":"47/moz-tools","topic_count":48,"__imported_original_data__":"{\"_cid\":45,\"_name\":\"Moz Tools\",\"_parentCid\":1000,\"_timestamp\":1296250950000,\"_slug\":\"moz-tools\",\"_order\":1,\"_description\":\"\"}","subCategoriesPerPage":15,"postQueue":0,"minTags":1,"maxTags":5,"totalPostCount":4100,"totalTopicCount":48},"value":53,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Getting Started","depth":1},{"bgColor":"#0a597c","cid":46,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss the Moz Pro tools with other users.","descriptionParsed":"<p dir=\"auto\">Discuss the Moz Pro tools with other users.<\/p>\n","disabled":0,"icon":"fa-line-chart","imageClass":"cover","isSection":0,"link":"","name":"Moz Pro","numRecentReplies":1,"order":2,"parentCid":47,"post_count":16556,"slug":"46/moz-pro","topic_count":3689,"__imported_original_data__":"{\"_cid\":44,\"_name\":\"Moz Pro\",\"_parentCid\":1000,\"_timestamp\":1296250950000,\"_slug\":\"moz-pro\",\"_order\":3,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":19716,"totalTopicCount":4403,"children":[{"bgColor":"#8772c1","cid":64,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Chat keyword research strategy and how Keyword Explorer helps you do your best work.","descriptionParsed":"<p dir=\"auto\">Chat keyword research strategy and how Keyword Explorer helps you do your best work.<\/p>\n","disabled":0,"icon":"fa-search","imageClass":"cover","isSection":0,"link":"","name":"Keyword Explorer","numRecentReplies":1,"order":3,"parentCid":46,"post_count":79,"slug":"64/keyword-explorer","topic_count":24,"__imported_original_data__":"{\"_cid\":85,\"_name\":\"Keyword Explorer\",\"_parentCid\":1000,\"_timestamp\":1618838033000,\"_slug\":\"keyword-explorer\",\"_order\":4,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":79,"totalTopicCount":24,"children":[],"parent":{"bgColor":"#0a597c","cid":46,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss the Moz Pro tools with other users.","descriptionParsed":"<p dir=\"auto\">Discuss the Moz Pro tools with other users.<\/p>\n","disabled":0,"icon":"fa-line-chart","imageClass":"cover","isSection":0,"link":"","name":"Moz Pro","numRecentReplies":1,"order":2,"parentCid":47,"post_count":16556,"slug":"46/moz-pro","topic_count":3689,"__imported_original_data__":"{\"_cid\":44,\"_name\":\"Moz Pro\",\"_parentCid\":1000,\"_timestamp\":1296250950000,\"_slug\":\"moz-pro\",\"_order\":3,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":16556,"totalTopicCount":3689},"value":64,"level":"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&bull; Keyword Explorer","depth":2},{"bgColor":"#575e66","cid":55,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Cover all things links and the industry-leading link data discoverable in Link Explorer.","descriptionParsed":"<p dir=\"auto\">Cover all things links and the industry-leading link data discoverable in Link Explorer.<\/p>\n","disabled":0,"icon":"fa-unlink","imageClass":"cover","isSection":0,"link":"","name":"Link Explorer","numRecentReplies":1,"order":4,"parentCid":46,"post_count":3081,"slug":"55/link-explorer","topic_count":690,"__imported_original_data__":"{\"_cid\":67,\"_name\":\"Link Explorer\",\"_parentCid\":1000,\"_timestamp\":1382446082000,\"_slug\":\"link-explorer\",\"_order\":5,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":3081,"totalTopicCount":690,"children":[],"parent":{"bgColor":"#0a597c","cid":46,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss the Moz Pro tools with other users.","descriptionParsed":"<p dir=\"auto\">Discuss the Moz Pro tools with other users.<\/p>\n","disabled":0,"icon":"fa-line-chart","imageClass":"cover","isSection":0,"link":"","name":"Moz Pro","numRecentReplies":1,"order":2,"parentCid":47,"post_count":16556,"slug":"46/moz-pro","topic_count":3689,"__imported_original_data__":"{\"_cid\":44,\"_name\":\"Moz Pro\",\"_parentCid\":1000,\"_timestamp\":1296250950000,\"_slug\":\"moz-pro\",\"_order\":3,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":16556,"totalTopicCount":3689},"value":55,"level":"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&bull; Link Explorer","depth":2}],"parent":{"bgColor":"#4dbdeb","cid":47,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Chat with the community about the Moz tools.","descriptionParsed":"<p dir=\"auto\">Chat with the community about the Moz tools.<\/p>\n","disabled":0,"icon":"fa-wrench","imageClass":"cover","isSection":0,"link":"","name":"Moz Tools","numRecentReplies":1,"order":1,"parentCid":0,"post_count":4100,"slug":"47/moz-tools","topic_count":48,"__imported_original_data__":"{\"_cid\":45,\"_name\":\"Moz Tools\",\"_parentCid\":1000,\"_timestamp\":1296250950000,\"_slug\":\"moz-tools\",\"_order\":1,\"_description\":\"\"}","subCategoriesPerPage":15,"postQueue":0,"minTags":1,"maxTags":5,"totalPostCount":4100,"totalTopicCount":48},"value":46,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Moz Pro","depth":1},{"bgColor":"#259983","cid":54,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss the Moz Local tool with other users.","descriptionParsed":"<p dir=\"auto\">Discuss the Moz Local tool with other users.<\/p>\n","disabled":0,"icon":"fa-map-pin","imageClass":"cover","isSection":0,"link":"","name":"Moz Local","numRecentReplies":1,"order":3,"parentCid":47,"post_count":1201,"slug":"54/moz-local","topic_count":363,"__imported_original_data__":"{\"_cid\":65,\"_name\":\"Moz Local\",\"_parentCid\":1000,\"_timestamp\":1382446082000,\"_slug\":\"moz-local\",\"_order\":7,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":1201,"totalTopicCount":363,"children":[],"parent":{"bgColor":"#4dbdeb","cid":47,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Chat with the community about the Moz tools.","descriptionParsed":"<p dir=\"auto\">Chat with the community about the Moz tools.<\/p>\n","disabled":0,"icon":"fa-wrench","imageClass":"cover","isSection":0,"link":"","name":"Moz Tools","numRecentReplies":1,"order":1,"parentCid":0,"post_count":4100,"slug":"47/moz-tools","topic_count":48,"__imported_original_data__":"{\"_cid\":45,\"_name\":\"Moz Tools\",\"_parentCid\":1000,\"_timestamp\":1296250950000,\"_slug\":\"moz-tools\",\"_order\":1,\"_description\":\"\"}","subCategoriesPerPage":15,"postQueue":0,"minTags":1,"maxTags":5,"totalPostCount":4100,"totalTopicCount":48},"value":54,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Moz Local","depth":1},{"bgColor":"#8772c1","cid":52,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Find insights and conversations specific to the Research Tools within Moz Pro.\t","descriptionParsed":"<p dir=\"auto\">Find insights and conversations specific to the Research Tools within Moz Pro.<\/p>\n","disabled":0,"icon":"fa-flask","imageClass":"cover","isSection":0,"link":"","name":"Moz Bar","numRecentReplies":1,"order":4,"parentCid":47,"post_count":4121,"slug":"52/moz-bar","topic_count":980,"__imported_original_data__":"{\"_cid\":59,\"_name\":\"Other Research Tools\",\"_parentCid\":1000,\"_timestamp\":1369824092000,\"_slug\":\"other-research-tools\",\"_order\":6,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":4121,"totalTopicCount":980,"children":[],"parent":{"bgColor":"#4dbdeb","cid":47,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Chat with the community about the Moz tools.","descriptionParsed":"<p dir=\"auto\">Chat with the community about the Moz tools.<\/p>\n","disabled":0,"icon":"fa-wrench","imageClass":"cover","isSection":0,"link":"","name":"Moz Tools","numRecentReplies":1,"order":1,"parentCid":0,"post_count":4100,"slug":"47/moz-tools","topic_count":48,"__imported_original_data__":"{\"_cid\":45,\"_name\":\"Moz Tools\",\"_parentCid\":1000,\"_timestamp\":1296250950000,\"_slug\":\"moz-tools\",\"_order\":1,\"_description\":\"\"}","subCategoriesPerPage":15,"postQueue":0,"minTags":1,"maxTags":5,"totalPostCount":4100,"totalTopicCount":48},"value":52,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Moz Bar","depth":1},{"bgColor":"#ff9f2c","cid":56,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss link data, metrics, and all of the calls available through the Links API. ","descriptionParsed":"<p dir=\"auto\">Discuss link data, metrics, and all of the calls available through the Links API.<\/p>\n","disabled":0,"icon":"fa-exchange","imageClass":"cover","isSection":0,"link":"","name":"API","numRecentReplies":1,"order":5,"parentCid":47,"post_count":979,"slug":"56/api","topic_count":229,"__imported_original_data__":"{\"_cid\":69,\"_name\":\"API\",\"_parentCid\":1000,\"_timestamp\":1382446082000,\"_slug\":\"api\",\"_order\":9,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":979,"totalTopicCount":229,"children":[],"parent":{"bgColor":"#4dbdeb","cid":47,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Chat with the community about the Moz tools.","descriptionParsed":"<p dir=\"auto\">Chat with the community about the Moz tools.<\/p>\n","disabled":0,"icon":"fa-wrench","imageClass":"cover","isSection":0,"link":"","name":"Moz Tools","numRecentReplies":1,"order":1,"parentCid":0,"post_count":4100,"slug":"47/moz-tools","topic_count":48,"__imported_original_data__":"{\"_cid\":45,\"_name\":\"Moz Tools\",\"_parentCid\":1000,\"_timestamp\":1296250950000,\"_slug\":\"moz-tools\",\"_order\":1,\"_description\":\"\"}","subCategoriesPerPage":15,"postQueue":0,"minTags":1,"maxTags":5,"totalPostCount":4100,"totalTopicCount":48},"value":56,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; API","depth":1}],"value":47,"level":"","text":"Moz Tools","depth":0},{"bgColor":"#fc4949","cid":9,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss the SEO process with fellow marketers","descriptionParsed":"<p dir=\"auto\">Discuss the SEO process with fellow marketers<\/p>\n","disabled":0,"icon":"fa-list-ol","imageClass":"cover","isSection":0,"link":"","name":"SEO Tactics","numRecentReplies":1,"order":2,"parentCid":0,"post_count":415,"slug":"9/seo-tactics","topic_count":63,"__imported_original_data__":"{\"_cid\":2000,\"_name\":\"The SEO Process\",\"_order\":2,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":15,"postQueue":1,"minTags":1,"maxTags":5,"totalPostCount":186923,"totalTopicCount":39327,"children":[{"bgColor":"#5dc93a","cid":10,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Ask and answer questions around the topic of content development for SEO.","descriptionParsed":"<p dir=\"auto\">Ask and answer questions around the topic of content development for SEO.<\/p>\n","disabled":0,"icon":"fa-newspaper-o","imageClass":"cover","isSection":0,"link":"","name":"Content Development","numRecentReplies":1,"order":1,"parentCid":9,"post_count":5684,"slug":"10/content-development","topic_count":1171,"__imported_original_data__":"{\"_cid\":2,\"_name\":\"Content & Blogging\",\"_parentCid\":2000,\"_timestamp\":1296250948000,\"_slug\":\"content-blogging\",\"_order\":1,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":5684,"totalTopicCount":1171,"children":[],"parent":{"bgColor":"#fc4949","cid":9,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss the SEO process with fellow marketers","descriptionParsed":"<p dir=\"auto\">Discuss the SEO process with fellow marketers<\/p>\n","disabled":0,"icon":"fa-list-ol","imageClass":"cover","isSection":0,"link":"","name":"SEO Tactics","numRecentReplies":1,"order":2,"parentCid":0,"post_count":415,"slug":"9/seo-tactics","topic_count":63,"__imported_original_data__":"{\"_cid\":2000,\"_name\":\"The SEO Process\",\"_order\":2,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":15,"postQueue":1,"minTags":1,"maxTags":5,"totalPostCount":415,"totalTopicCount":63},"value":10,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Content Development","depth":1},{"bgColor":"#4ebdea","cid":19,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Uncover new and exciting ways to conduct competitive analysis","descriptionParsed":"<p dir=\"auto\">Uncover new and exciting ways to conduct competitive analysis<\/p>\n","disabled":0,"icon":"fa-binoculars","imageClass":"cover","isSection":0,"link":"","name":"Competitive Research","numRecentReplies":1,"order":2,"parentCid":9,"post_count":3237,"slug":"19/competitive-research","topic_count":677,"__imported_original_data__":"{\"_cid\":12,\"_name\":\"Competitive Research\",\"_parentCid\":3000,\"_timestamp\":1296250949000,\"_slug\":\"competitive-research\",\"_order\":3,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":3237,"totalTopicCount":677,"children":[],"parent":{"bgColor":"#fc4949","cid":9,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss the SEO process with fellow marketers","descriptionParsed":"<p dir=\"auto\">Discuss the SEO process with fellow marketers<\/p>\n","disabled":0,"icon":"fa-list-ol","imageClass":"cover","isSection":0,"link":"","name":"SEO Tactics","numRecentReplies":1,"order":2,"parentCid":0,"post_count":415,"slug":"9/seo-tactics","topic_count":63,"__imported_original_data__":"{\"_cid\":2000,\"_name\":\"The SEO Process\",\"_order\":2,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":15,"postQueue":1,"minTags":1,"maxTags":5,"totalPostCount":415,"totalTopicCount":63},"value":19,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Competitive Research","depth":1},{"bgColor":"#8772c1","cid":12,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Learn about keyword research best practices and how to improve your keyword strategy.","descriptionParsed":"<p dir=\"auto\">Learn about keyword research best practices and how to improve your keyword strategy.<\/p>\n","disabled":0,"icon":"fa-flask","imageClass":"cover","isSection":0,"link":"","name":"Keyword Research","numRecentReplies":1,"order":3,"parentCid":9,"post_count":5075,"slug":"12/keyword-research","topic_count":1131,"__imported_original_data__":"{\"_cid\":4,\"_name\":\"Keyword Research\",\"_parentCid\":2000,\"_timestamp\":1296250948000,\"_slug\":\"keyword-research\",\"_order\":3,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":5075,"totalTopicCount":1131,"children":[],"parent":{"bgColor":"#fc4949","cid":9,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss the SEO process with fellow marketers","descriptionParsed":"<p dir=\"auto\">Discuss the SEO process with fellow marketers<\/p>\n","disabled":0,"icon":"fa-list-ol","imageClass":"cover","isSection":0,"link":"","name":"SEO Tactics","numRecentReplies":1,"order":2,"parentCid":0,"post_count":415,"slug":"9/seo-tactics","topic_count":63,"__imported_original_data__":"{\"_cid\":2000,\"_name\":\"The SEO Process\",\"_order\":2,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":15,"postQueue":1,"minTags":1,"maxTags":5,"totalPostCount":415,"totalTopicCount":63},"value":12,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Keyword Research","depth":1},{"bgColor":"#ff9f2c","cid":13,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Chat through link building best practices and outreach techniques.","descriptionParsed":"<p dir=\"auto\">Chat through link building best practices and outreach techniques.<\/p>\n","disabled":0,"icon":"fa-link","imageClass":"cover","isSection":0,"link":"","name":"Link Building","numRecentReplies":1,"order":4,"parentCid":9,"post_count":23431,"slug":"13/link-building","topic_count":4592,"__imported_original_data__":"{\"_cid\":5,\"_name\":\"Link Building\",\"_parentCid\":2000,\"_timestamp\":1296250948000,\"_slug\":\"link-building\",\"_order\":4,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":23431,"totalTopicCount":4592,"children":[],"parent":{"bgColor":"#fc4949","cid":9,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss the SEO process with fellow marketers","descriptionParsed":"<p dir=\"auto\">Discuss the SEO process with fellow marketers<\/p>\n","disabled":0,"icon":"fa-list-ol","imageClass":"cover","isSection":0,"link":"","name":"SEO Tactics","numRecentReplies":1,"order":2,"parentCid":0,"post_count":415,"slug":"9/seo-tactics","topic_count":63,"__imported_original_data__":"{\"_cid\":2000,\"_name\":\"The SEO Process\",\"_order\":2,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":15,"postQueue":1,"minTags":1,"maxTags":5,"totalPostCount":415,"totalTopicCount":63},"value":13,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Link Building","depth":1},{"bgColor":"#575e66","cid":11,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Explore on-page optimization and its role in a larger SEO strategy.","descriptionParsed":"<p dir=\"auto\">Explore on-page optimization and its role in a larger SEO strategy.<\/p>\n","disabled":0,"icon":"fa-sliders","imageClass":"cover","isSection":0,"link":"","name":"On-Page Optimization","numRecentReplies":1,"order":5,"parentCid":9,"post_count":22852,"slug":"11/on-page-optimization","topic_count":4874,"__imported_original_data__":"{\"_cid\":3,\"_name\":\"On-Page / Site Optimization\",\"_parentCid\":2000,\"_timestamp\":1296250948000,\"_slug\":\"on-page-site-optimization\",\"_order\":2,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":22852,"totalTopicCount":4874,"children":[],"parent":{"bgColor":"#fc4949","cid":9,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss the SEO process with fellow marketers","descriptionParsed":"<p dir=\"auto\">Discuss the SEO process with fellow marketers<\/p>\n","disabled":0,"icon":"fa-list-ol","imageClass":"cover","isSection":0,"link":"","name":"SEO Tactics","numRecentReplies":1,"order":2,"parentCid":0,"post_count":415,"slug":"9/seo-tactics","topic_count":63,"__imported_original_data__":"{\"_cid\":2000,\"_name\":\"The SEO Process\",\"_order\":2,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":15,"postQueue":1,"minTags":1,"maxTags":5,"totalPostCount":415,"totalTopicCount":63},"value":11,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; On-Page Optimization","depth":1},{"bgColor":"#0075a8","cid":15,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss site health, structure, and other technical SEO strategies.","descriptionParsed":"<p dir=\"auto\">Discuss site health, structure, and other technical SEO strategies.<\/p>\n","disabled":0,"icon":"fa-desktop","imageClass":"cover","isSection":0,"link":"","name":"Technical SEO","numRecentReplies":1,"order":6,"parentCid":9,"post_count":46593,"slug":"15/technical-seo","topic_count":9885,"__imported_original_data__":"{\"_cid\":7,\"_name\":\"Technical SEO Issues\",\"_parentCid\":2000,\"_timestamp\":1296250949000,\"_slug\":\"technical-seo-issues\",\"_order\":6,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":46593,"totalTopicCount":9885,"children":[],"parent":{"bgColor":"#fc4949","cid":9,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss the SEO process with fellow marketers","descriptionParsed":"<p dir=\"auto\">Discuss the SEO process with fellow marketers<\/p>\n","disabled":0,"icon":"fa-list-ol","imageClass":"cover","isSection":0,"link":"","name":"SEO Tactics","numRecentReplies":1,"order":2,"parentCid":0,"post_count":415,"slug":"9/seo-tactics","topic_count":63,"__imported_original_data__":"{\"_cid\":2000,\"_name\":\"The SEO Process\",\"_order\":2,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":15,"postQueue":1,"minTags":1,"maxTags":5,"totalPostCount":415,"totalTopicCount":63},"value":15,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Technical SEO","depth":1},{"bgColor":"#ffd262","cid":6,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss the best ways to report on performance and communicate results to stakeholders.","descriptionParsed":"<p dir=\"auto\">Discuss the best ways to report on performance and communicate results to stakeholders.<\/p>\n","disabled":0,"icon":"fa-line-chart","imageClass":"cover","isSection":0,"link":"","name":"Reporting &amp; Analytics","numRecentReplies":1,"order":7,"parentCid":9,"post_count":9918,"slug":"6/reporting-analytics","topic_count":2159,"__imported_original_data__":"{\"_cid\":3000,\"_name\":\"Measuring & Testing\",\"_order\":3,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":9918,"totalTopicCount":2159,"children":[],"parent":{"bgColor":"#fc4949","cid":9,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss the SEO process with fellow marketers","descriptionParsed":"<p dir=\"auto\">Discuss the SEO process with fellow marketers<\/p>\n","disabled":0,"icon":"fa-list-ol","imageClass":"cover","isSection":0,"link":"","name":"SEO Tactics","numRecentReplies":1,"order":2,"parentCid":0,"post_count":415,"slug":"9/seo-tactics","topic_count":63,"__imported_original_data__":"{\"_cid\":2000,\"_name\":\"The SEO Process\",\"_order\":2,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":15,"postQueue":1,"minTags":1,"maxTags":5,"totalPostCount":415,"totalTopicCount":63},"value":6,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Reporting &amp; Analytics","depth":1},{"bgColor":"#fc4949","cid":16,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Looking to level up your SEO techniques? Chat through more advanced approaches.","descriptionParsed":"<p dir=\"auto\">Looking to level up your SEO techniques? Chat through more advanced approaches.<\/p>\n","disabled":0,"icon":"fa-graduation-cap","imageClass":"cover","isSection":0,"link":"","name":"Intermediate &amp; Advanced SEO","numRecentReplies":1,"order":8,"parentCid":9,"post_count":51901,"slug":"16/intermediate-advanced-seo","topic_count":11073,"__imported_original_data__":"{\"_cid\":8,\"_name\":\"Intermediate & Advanced SEO\",\"_parentCid\":2000,\"_timestamp\":1296250949000,\"_slug\":\"intermediate-advanced-seo\",\"_order\":7,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":51901,"totalTopicCount":11073,"children":[],"parent":{"bgColor":"#fc4949","cid":9,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss the SEO process with fellow marketers","descriptionParsed":"<p dir=\"auto\">Discuss the SEO process with fellow marketers<\/p>\n","disabled":0,"icon":"fa-list-ol","imageClass":"cover","isSection":0,"link":"","name":"SEO Tactics","numRecentReplies":1,"order":2,"parentCid":0,"post_count":415,"slug":"9/seo-tactics","topic_count":63,"__imported_original_data__":"{\"_cid\":2000,\"_name\":\"The SEO Process\",\"_order\":2,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":15,"postQueue":1,"minTags":1,"maxTags":5,"totalPostCount":415,"totalTopicCount":63},"value":16,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Intermediate &amp; Advanced SEO","depth":1},{"bgColor":"#4ebdea","cid":14,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Explore how to optimize your website&#x27;s images and videos for search.","descriptionParsed":"<p dir=\"auto\">Explore how to optimize your website's images and videos for search.<\/p>\n","disabled":0,"icon":"fa-video-camera","imageClass":"cover","isSection":0,"link":"","name":"Image &amp; Video Optimization","numRecentReplies":1,"order":9,"parentCid":9,"post_count":3919,"slug":"14/image-video-optimization","topic_count":803,"__imported_original_data__":"{\"_cid\":6,\"_name\":\"Vertical SEO: Video, Image, Local\",\"_parentCid\":2000,\"_timestamp\":1296250949000,\"_slug\":\"vertical-seo-video-image-local\",\"_order\":5,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":3919,"totalTopicCount":803,"children":[],"parent":{"bgColor":"#fc4949","cid":9,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss the SEO process with fellow marketers","descriptionParsed":"<p dir=\"auto\">Discuss the SEO process with fellow marketers<\/p>\n","disabled":0,"icon":"fa-list-ol","imageClass":"cover","isSection":0,"link":"","name":"SEO Tactics","numRecentReplies":1,"order":2,"parentCid":0,"post_count":415,"slug":"9/seo-tactics","topic_count":63,"__imported_original_data__":"{\"_cid\":2000,\"_name\":\"The SEO Process\",\"_order\":2,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":15,"postQueue":1,"minTags":1,"maxTags":5,"totalPostCount":415,"totalTopicCount":63},"value":14,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Image &amp; Video Optimization","depth":1},{"bgColor":"#5dc93a","cid":22,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discussions around international SEO tactics.","descriptionParsed":"<p dir=\"auto\">Discussions around international SEO tactics.<\/p>\n","disabled":0,"icon":"fa-globe","imageClass":"cover","isSection":0,"link":"","name":"International SEO","numRecentReplies":1,"order":10,"parentCid":9,"post_count":3363,"slug":"22/international-seo","topic_count":765,"__imported_original_data__":"{\"_cid\":16,\"_name\":\"International Issues\",\"_parentCid\":4000,\"_timestamp\":1296250949000,\"_slug\":\"international-issues\",\"_order\":2,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":3363,"totalTopicCount":765,"children":[],"parent":{"bgColor":"#fc4949","cid":9,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss the SEO process with fellow marketers","descriptionParsed":"<p dir=\"auto\">Discuss the SEO process with fellow marketers<\/p>\n","disabled":0,"icon":"fa-list-ol","imageClass":"cover","isSection":0,"link":"","name":"SEO Tactics","numRecentReplies":1,"order":2,"parentCid":0,"post_count":415,"slug":"9/seo-tactics","topic_count":63,"__imported_original_data__":"{\"_cid\":2000,\"_name\":\"The SEO Process\",\"_order\":2,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":15,"postQueue":1,"minTags":1,"maxTags":5,"totalPostCount":415,"totalTopicCount":63},"value":22,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; International SEO","depth":1},{"bgColor":"#259983","cid":5,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"So much goes into building a comprehensive local marketing strategy. Discuss all things local with other marketing professionals.","descriptionParsed":"<p dir=\"auto\">So much goes into building a comprehensive local marketing strategy. Discuss all things local with other marketing professionals.<\/p>\n","disabled":0,"icon":"fa-street-view","imageClass":"cover","isSection":0,"link":"","name":"Local SEO","numRecentReplies":1,"order":11,"parentCid":9,"post_count":1746,"slug":"5/local-seo","topic_count":352,"__imported_original_data__":"{\"_cid\":8000,\"_name\":\"Local Marketing\",\"_order\":8,\"_timestamp\":1389105256000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":10535,"totalTopicCount":2134,"children":[{"bgColor":"#575e66","cid":59,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Examine the impact of maintaining consistent and accurate local listings on your local SEO strategy.","descriptionParsed":"<p dir=\"auto\">Examine the impact of maintaining consistent and accurate local listings on your local SEO strategy.<\/p>\n","disabled":0,"icon":"fa-list","imageClass":"cover","isSection":0,"link":"","name":"Local Listings","numRecentReplies":1,"order":1,"parentCid":5,"post_count":4584,"slug":"59/local-listings","topic_count":927,"__imported_original_data__":"{\"_cid\":75,\"_name\":\"Local Listings\",\"_parentCid\":8000,\"_timestamp\":1389105256000,\"_slug\":\"local-listings\",\"_order\":3,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":4584,"totalTopicCount":927,"children":[],"parent":{"bgColor":"#259983","cid":5,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"So much goes into building a comprehensive local marketing strategy. Discuss all things local with other marketing professionals.","descriptionParsed":"<p dir=\"auto\">So much goes into building a comprehensive local marketing strategy. Discuss all things local with other marketing professionals.<\/p>\n","disabled":0,"icon":"fa-street-view","imageClass":"cover","isSection":0,"link":"","name":"Local SEO","numRecentReplies":1,"order":11,"parentCid":9,"post_count":1746,"slug":"5/local-seo","topic_count":352,"__imported_original_data__":"{\"_cid\":8000,\"_name\":\"Local Marketing\",\"_order\":8,\"_timestamp\":1389105256000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":1746,"totalTopicCount":352},"value":59,"level":"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&bull; Local Listings","depth":2},{"bgColor":"#ffd262","cid":60,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Dive into how to manage reviews and ratings for your local marketing strategy.","descriptionParsed":"<p dir=\"auto\">Dive into how to manage reviews and ratings for your local marketing strategy.<\/p>\n","disabled":0,"icon":"fa-star","imageClass":"cover","isSection":0,"link":"","name":"Reviews and Ratings","numRecentReplies":1,"order":2,"parentCid":5,"post_count":1168,"slug":"60/reviews-and-ratings","topic_count":237,"__imported_original_data__":"{\"_cid\":77,\"_name\":\"Reviews and Ratings\",\"_parentCid\":8000,\"_timestamp\":1389105256000,\"_slug\":\"reviews-and-ratings\",\"_order\":4,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":1168,"totalTopicCount":237,"children":[],"parent":{"bgColor":"#259983","cid":5,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"So much goes into building a comprehensive local marketing strategy. Discuss all things local with other marketing professionals.","descriptionParsed":"<p dir=\"auto\">So much goes into building a comprehensive local marketing strategy. Discuss all things local with other marketing professionals.<\/p>\n","disabled":0,"icon":"fa-street-view","imageClass":"cover","isSection":0,"link":"","name":"Local SEO","numRecentReplies":1,"order":11,"parentCid":9,"post_count":1746,"slug":"5/local-seo","topic_count":352,"__imported_original_data__":"{\"_cid\":8000,\"_name\":\"Local Marketing\",\"_order\":8,\"_timestamp\":1389105256000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":1746,"totalTopicCount":352},"value":60,"level":"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&bull; Reviews and Ratings","depth":2},{"bgColor":"#0075a8","cid":58,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Considering local SEO and its impact on your website? Discuss website optimization for local SEO.","descriptionParsed":"<p dir=\"auto\">Considering local SEO and its impact on your website? Discuss website optimization for local SEO.<\/p>\n","disabled":0,"icon":"fa-sticky-note","imageClass":"cover","isSection":0,"link":"","name":"Local Website Optimization","numRecentReplies":1,"order":3,"parentCid":5,"post_count":3037,"slug":"58/local-website-optimization","topic_count":618,"__imported_original_data__":"{\"_cid\":73,\"_name\":\"Local Website Optimization\",\"_parentCid\":8000,\"_timestamp\":1389105256000,\"_slug\":\"local-website-optimization\",\"_order\":2,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":3037,"totalTopicCount":618,"children":[],"parent":{"bgColor":"#259983","cid":5,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"So much goes into building a comprehensive local marketing strategy. Discuss all things local with other marketing professionals.","descriptionParsed":"<p dir=\"auto\">So much goes into building a comprehensive local marketing strategy. Discuss all things local with other marketing professionals.<\/p>\n","disabled":0,"icon":"fa-street-view","imageClass":"cover","isSection":0,"link":"","name":"Local SEO","numRecentReplies":1,"order":11,"parentCid":9,"post_count":1746,"slug":"5/local-seo","topic_count":352,"__imported_original_data__":"{\"_cid\":8000,\"_name\":\"Local Marketing\",\"_order\":8,\"_timestamp\":1389105256000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":1746,"totalTopicCount":352},"value":58,"level":"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&bull; Local Website Optimization","depth":2}],"parent":{"bgColor":"#fc4949","cid":9,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss the SEO process with fellow marketers","descriptionParsed":"<p dir=\"auto\">Discuss the SEO process with fellow marketers<\/p>\n","disabled":0,"icon":"fa-list-ol","imageClass":"cover","isSection":0,"link":"","name":"SEO Tactics","numRecentReplies":1,"order":2,"parentCid":0,"post_count":415,"slug":"9/seo-tactics","topic_count":63,"__imported_original_data__":"{\"_cid\":2000,\"_name\":\"The SEO Process\",\"_order\":2,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":15,"postQueue":1,"minTags":1,"maxTags":5,"totalPostCount":415,"totalTopicCount":63},"value":5,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Local SEO","depth":1}],"value":9,"level":"","text":"SEO Tactics","depth":0},{"bgColor":"#ff9f2c","cid":3,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss industry events, jobs, and news!","descriptionParsed":"<p dir=\"auto\">Discuss industry events, jobs, and news!<\/p>\n","disabled":0,"icon":"fa-users","imageClass":"cover","isSection":0,"link":"","name":"Community","numRecentReplies":1,"order":3,"parentCid":0,"post_count":107,"slug":"3/community","topic_count":17,"__imported_original_data__":"{\"_cid\":6000,\"_name\":\"Community\",\"_order\":6,\"_timestamp\":1296250950000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"postQueue":1,"minTags":1,"maxTags":5,"totalPostCount":3810,"totalTopicCount":686,"children":[{"bgColor":"#4ebdea","cid":48,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Learn about news around the Mozplex and projects that Mozzers are working on.","descriptionParsed":"<p dir=\"auto\">Learn about news around the Mozplex and projects that Mozzers are working on.<\/p>\n","disabled":0,"icon":"fa-bullhorn","imageClass":"cover","isSection":0,"link":"","name":"Moz News","numRecentReplies":1,"order":2,"parentCid":3,"post_count":135,"slug":"48/moz-news","topic_count":7,"__imported_original_data__":"{\"_cid\":46,\"_name\":\"Moz News\",\"_parentCid\":6000,\"_timestamp\":1296250950000,\"_slug\":\"moz-news\",\"_order\":7,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":135,"totalTopicCount":7,"children":[],"parent":{"bgColor":"#ff9f2c","cid":3,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss industry events, jobs, and news!","descriptionParsed":"<p dir=\"auto\">Discuss industry events, jobs, and news!<\/p>\n","disabled":0,"icon":"fa-users","imageClass":"cover","isSection":0,"link":"","name":"Community","numRecentReplies":1,"order":3,"parentCid":0,"post_count":107,"slug":"3/community","topic_count":17,"__imported_original_data__":"{\"_cid\":6000,\"_name\":\"Community\",\"_order\":6,\"_timestamp\":1296250950000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"postQueue":1,"minTags":1,"maxTags":5,"totalPostCount":107,"totalTopicCount":17},"value":48,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Moz News","depth":1},{"bgColor":"#5dc93a","cid":44,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss upcoming industry news and events","descriptionParsed":"<p dir=\"auto\">Discuss upcoming industry news and events<\/p>\n","disabled":0,"icon":"fa-arrow-circle-o-down","imageClass":"cover","isSection":0,"link":"","name":"Industry News","numRecentReplies":1,"order":3,"parentCid":3,"post_count":2923,"slug":"44/industry-news","topic_count":542,"__imported_original_data__":"{\"_cid\":41,\"_name\":\"Inbound Marketing Industry\",\"_parentCid\":6000,\"_timestamp\":1296250950000,\"_slug\":\"inbound-marketing-industry\",\"_order\":5,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":3387,"totalTopicCount":639,"children":[{"bgColor":"#8772c1","cid":40,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Upcoming industry events","descriptionParsed":"<p dir=\"auto\">Upcoming industry events<\/p>\n","disabled":0,"icon":"fa-comment","imageClass":"cover","isSection":0,"link":"","name":"Industry Events","numRecentReplies":1,"order":3,"parentCid":44,"post_count":464,"slug":"40/industry-events","topic_count":97,"__imported_original_data__":"{\"_cid\":37,\"_name\":\"Inbound Marketing Events\",\"_parentCid\":6000,\"_timestamp\":1296250949000,\"_slug\":\"inbound-marketing-events\",\"_order\":1,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":464,"totalTopicCount":97,"children":[],"parent":{"bgColor":"#5dc93a","cid":44,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss upcoming industry news and events","descriptionParsed":"<p dir=\"auto\">Discuss upcoming industry news and events<\/p>\n","disabled":0,"icon":"fa-arrow-circle-o-down","imageClass":"cover","isSection":0,"link":"","name":"Industry News","numRecentReplies":1,"order":3,"parentCid":3,"post_count":2923,"slug":"44/industry-news","topic_count":542,"__imported_original_data__":"{\"_cid\":41,\"_name\":\"Inbound Marketing Industry\",\"_parentCid\":6000,\"_timestamp\":1296250950000,\"_slug\":\"inbound-marketing-industry\",\"_order\":5,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":2923,"totalTopicCount":542},"value":40,"level":"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&bull; Industry Events","depth":2}],"parent":{"bgColor":"#ff9f2c","cid":3,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss industry events, jobs, and news!","descriptionParsed":"<p dir=\"auto\">Discuss industry events, jobs, and news!<\/p>\n","disabled":0,"icon":"fa-users","imageClass":"cover","isSection":0,"link":"","name":"Community","numRecentReplies":1,"order":3,"parentCid":0,"post_count":107,"slug":"3/community","topic_count":17,"__imported_original_data__":"{\"_cid\":6000,\"_name\":\"Community\",\"_order\":6,\"_timestamp\":1296250950000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"postQueue":1,"minTags":1,"maxTags":5,"totalPostCount":107,"totalTopicCount":17},"value":44,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Industry News","depth":1},{"bgColor":"#259983","cid":43,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Looking to hire an SEO? Have a special opportunity to share with other SEO professionals? Share them here!","descriptionParsed":"<p dir=\"auto\">Looking to hire an SEO? Have a special opportunity to share with other SEO professionals? Share them here!<\/p>\n","disabled":0,"icon":"fa-suitcase","imageClass":"cover","isSection":0,"link":"","name":"Jobs and Opportunities","numRecentReplies":1,"order":4,"parentCid":3,"post_count":181,"slug":"43/jobs-and-opportunities","topic_count":23,"__imported_original_data__":"{\"_cid\":40,\"_name\":\"Interviews\",\"_parentCid\":6000,\"_timestamp\":1296250950000,\"_slug\":\"interviews\",\"_order\":4,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":181,"totalTopicCount":23,"children":[],"parent":{"bgColor":"#ff9f2c","cid":3,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss industry events, jobs, and news!","descriptionParsed":"<p dir=\"auto\">Discuss industry events, jobs, and news!<\/p>\n","disabled":0,"icon":"fa-users","imageClass":"cover","isSection":0,"link":"","name":"Community","numRecentReplies":1,"order":3,"parentCid":0,"post_count":107,"slug":"3/community","topic_count":17,"__imported_original_data__":"{\"_cid\":6000,\"_name\":\"Community\",\"_order\":6,\"_timestamp\":1296250950000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"postQueue":1,"minTags":1,"maxTags":5,"totalPostCount":107,"totalTopicCount":17},"value":43,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Jobs and Opportunities","depth":1}],"value":3,"level":"","text":"Community","depth":0},{"bgColor":"#8772c1","cid":7,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Chat about tactics outside of SEO","descriptionParsed":"<p dir=\"auto\">Chat about tactics outside of SEO<\/p>\n","disabled":0,"icon":"fa-eye","imageClass":"cover","isSection":0,"link":"","name":"Digital Marketing","numRecentReplies":1,"order":4,"parentCid":0,"post_count":16,"slug":"7/digital-marketing","topic_count":3,"__imported_original_data__":"{\"_cid\":7000,\"_name\":\"Online Marketing\",\"_order\":7,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":23679,"totalTopicCount":5095,"children":[{"bgColor":"#16b7df","cid":33,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Do you work in affiliate marketing? Share the latest and get your questions answered.","descriptionParsed":"<p dir=\"auto\">Do you work in affiliate marketing? Share the latest and get your questions answered.<\/p>\n","disabled":0,"icon":"fa-black-tie","imageClass":"cover","isSection":0,"link":"","name":"Affiliate Marketing","numRecentReplies":1,"order":1,"parentCid":7,"post_count":950,"slug":"33/affiliate-marketing","topic_count":227,"__imported_original_data__":"{\"_cid\":28,\"_name\":\"Affiliate Marketing\",\"_parentCid\":7000,\"_timestamp\":1296250949000,\"_slug\":\"affiliate-marketing\",\"_order\":7,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":950,"totalTopicCount":227,"children":[],"parent":{"bgColor":"#8772c1","cid":7,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Chat about tactics outside of SEO","descriptionParsed":"<p dir=\"auto\">Chat about tactics outside of SEO<\/p>\n","disabled":0,"icon":"fa-eye","imageClass":"cover","isSection":0,"link":"","name":"Digital Marketing","numRecentReplies":1,"order":4,"parentCid":0,"post_count":16,"slug":"7/digital-marketing","topic_count":3,"__imported_original_data__":"{\"_cid\":7000,\"_name\":\"Online Marketing\",\"_order\":7,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":16,"totalTopicCount":3},"value":33,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Affiliate Marketing","depth":1},{"bgColor":"#5ec93a","cid":31,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Explore the topics of branding and brand awareness and why they’re important for any business.","descriptionParsed":"<p dir=\"auto\">Explore the topics of branding and brand awareness and why they’re important for any business.<\/p>\n","disabled":0,"icon":"fa-flag","imageClass":"cover","isSection":0,"link":"","name":"Branding","numRecentReplies":1,"order":2,"parentCid":7,"post_count":3557,"slug":"31/branding","topic_count":746,"__imported_original_data__":"{\"_cid\":26,\"_name\":\"Branding / Brand Awareness\",\"_parentCid\":7000,\"_timestamp\":1296250949000,\"_slug\":\"branding-brand-awareness\",\"_order\":5,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":3557,"totalTopicCount":746,"children":[],"parent":{"bgColor":"#8772c1","cid":7,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Chat about tactics outside of SEO","descriptionParsed":"<p dir=\"auto\">Chat about tactics outside of SEO<\/p>\n","disabled":0,"icon":"fa-eye","imageClass":"cover","isSection":0,"link":"","name":"Digital Marketing","numRecentReplies":1,"order":4,"parentCid":0,"post_count":16,"slug":"7/digital-marketing","topic_count":3,"__imported_original_data__":"{\"_cid\":7000,\"_name\":\"Online Marketing\",\"_order\":7,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":16,"totalTopicCount":3},"value":31,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Branding","depth":1},{"bgColor":"#ff9f2c","cid":34,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Chat through best practices for conversion rate optimization.","descriptionParsed":"<p dir=\"auto\">Chat through best practices for conversion rate optimization.<\/p>\n","disabled":0,"icon":"fa-share","imageClass":"cover","isSection":0,"link":"","name":"Conversion Rate Optimization","numRecentReplies":1,"order":3,"parentCid":7,"post_count":2207,"slug":"34/conversion-rate-optimization","topic_count":461,"__imported_original_data__":"{\"_cid\":29,\"_name\":\"Conversion Rate Optimization\",\"_parentCid\":7000,\"_timestamp\":1296250949000,\"_slug\":\"conversion-rate-optimization\",\"_order\":8,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":2207,"totalTopicCount":461,"children":[],"parent":{"bgColor":"#8772c1","cid":7,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Chat about tactics outside of SEO","descriptionParsed":"<p dir=\"auto\">Chat about tactics outside of SEO<\/p>\n","disabled":0,"icon":"fa-eye","imageClass":"cover","isSection":0,"link":"","name":"Digital Marketing","numRecentReplies":1,"order":4,"parentCid":0,"post_count":16,"slug":"7/digital-marketing","topic_count":3,"__imported_original_data__":"{\"_cid\":7000,\"_name\":\"Online Marketing\",\"_order\":7,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":16,"totalTopicCount":3},"value":34,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Conversion Rate Optimization","depth":1},{"bgColor":"#259983","cid":25,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Talk through the latest in web design and development trends.","descriptionParsed":"<p dir=\"auto\">Talk through the latest in web design and development trends.<\/p>\n","disabled":0,"icon":"fa-desktop","imageClass":"cover","isSection":0,"link":"","name":"Web Design","numRecentReplies":1,"order":4,"parentCid":7,"post_count":8138,"slug":"25/web-design","topic_count":1711,"__imported_original_data__":"{\"_cid\":19,\"_name\":\"Web Design\",\"_parentCid\":4000,\"_timestamp\":1296250949000,\"_slug\":\"web-design\",\"_order\":5,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":8138,"totalTopicCount":1711,"children":[],"parent":{"bgColor":"#8772c1","cid":7,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Chat about tactics outside of SEO","descriptionParsed":"<p dir=\"auto\">Chat about tactics outside of SEO<\/p>\n","disabled":0,"icon":"fa-eye","imageClass":"cover","isSection":0,"link":"","name":"Digital Marketing","numRecentReplies":1,"order":4,"parentCid":0,"post_count":16,"slug":"7/digital-marketing","topic_count":3,"__imported_original_data__":"{\"_cid\":7000,\"_name\":\"Online Marketing\",\"_order\":7,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":16,"totalTopicCount":3},"value":25,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Web Design","depth":1},{"bgColor":"#8772c1","cid":29,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Examine the impact of paid search marketing and its relationship with organic search.","descriptionParsed":"<p dir=\"auto\">Examine the impact of paid search marketing and its relationship with organic search.<\/p>\n","disabled":0,"icon":"fa-money","imageClass":"cover","isSection":0,"link":"","name":"Paid Search Marketing","numRecentReplies":1,"order":5,"parentCid":7,"post_count":2615,"slug":"29/paid-search-marketing","topic_count":564,"__imported_original_data__":"{\"_cid\":24,\"_name\":\"Paid Search Marketing\",\"_parentCid\":7000,\"_timestamp\":1296250949000,\"_slug\":\"paid-search-marketing\",\"_order\":3,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":2615,"totalTopicCount":564,"children":[],"parent":{"bgColor":"#8772c1","cid":7,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Chat about tactics outside of SEO","descriptionParsed":"<p dir=\"auto\">Chat about tactics outside of SEO<\/p>\n","disabled":0,"icon":"fa-eye","imageClass":"cover","isSection":0,"link":"","name":"Digital Marketing","numRecentReplies":1,"order":4,"parentCid":0,"post_count":16,"slug":"7/digital-marketing","topic_count":3,"__imported_original_data__":"{\"_cid\":7000,\"_name\":\"Online Marketing\",\"_order\":7,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":16,"totalTopicCount":3},"value":29,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Paid Search Marketing","depth":1},{"bgColor":"#fc4949","cid":27,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss the impact of growing social media presence and its relationship with other digital strategies.","descriptionParsed":"<p dir=\"auto\">Discuss the impact of growing social media presence and its relationship with other digital strategies.<\/p>\n","disabled":0,"icon":"fa-thumbs-up","imageClass":"cover","isSection":0,"link":"","name":"Social Media","numRecentReplies":1,"order":6,"parentCid":7,"post_count":6196,"slug":"27/social-media","topic_count":1383,"__imported_original_data__":"{\"_cid\":22,\"_name\":\"Social Media\",\"_parentCid\":7000,\"_timestamp\":1296250949000,\"_slug\":\"social-media\",\"_order\":1,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":6196,"totalTopicCount":1383,"children":[],"parent":{"bgColor":"#8772c1","cid":7,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Chat about tactics outside of SEO","descriptionParsed":"<p dir=\"auto\">Chat about tactics outside of SEO<\/p>\n","disabled":0,"icon":"fa-eye","imageClass":"cover","isSection":0,"link":"","name":"Digital Marketing","numRecentReplies":1,"order":4,"parentCid":0,"post_count":16,"slug":"7/digital-marketing","topic_count":3,"__imported_original_data__":"{\"_cid\":7000,\"_name\":\"Online Marketing\",\"_order\":7,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":16,"totalTopicCount":3},"value":27,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Social Media","depth":1}],"value":7,"level":"","text":"Digital Marketing","depth":0},{"bgColor":"#5dc93a","cid":8,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Dive into research and trends in the search industry.","descriptionParsed":"<p dir=\"auto\">Dive into research and trends in the search industry.<\/p>\n","disabled":0,"icon":"fa-area-chart","imageClass":"cover","isSection":0,"link":"","name":"Research &amp; Trends","numRecentReplies":1,"order":5,"parentCid":0,"post_count":1,"slug":"8/research-trends","topic_count":1,"__imported_original_data__":"{\"_cid\":4000,\"_name\":\"Research & Trends\",\"_order\":4,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":21089,"totalTopicCount":4403,"children":[{"bgColor":"#ffd262","cid":26,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss new SERP trends","descriptionParsed":"<p dir=\"auto\">Discuss new SERP trends<\/p>\n","disabled":0,"icon":"fa-search","imageClass":"cover","isSection":0,"link":"","name":"SERP Trends","numRecentReplies":1,"order":1,"parentCid":8,"post_count":700,"slug":"26/serp-trends","topic_count":164,"__imported_original_data__":"{\"_cid\":20,\"_name\":\"Alternative Search Sources\",\"_parentCid\":4000,\"_timestamp\":1296250949000,\"_slug\":\"alternative-search-sources\",\"_order\":6,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":700,"totalTopicCount":164,"children":[],"parent":{"bgColor":"#5dc93a","cid":8,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Dive into research and trends in the search industry.","descriptionParsed":"<p dir=\"auto\">Dive into research and trends in the search industry.<\/p>\n","disabled":0,"icon":"fa-area-chart","imageClass":"cover","isSection":0,"link":"","name":"Research &amp; Trends","numRecentReplies":1,"order":5,"parentCid":0,"post_count":1,"slug":"8/research-trends","topic_count":1,"__imported_original_data__":"{\"_cid\":4000,\"_name\":\"Research & Trends\",\"_order\":4,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":1,"totalTopicCount":1},"value":26,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; SERP Trends","depth":1},{"bgColor":"#fc4949","cid":21,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Learn more about search behavior and search trends.","descriptionParsed":"<p dir=\"auto\">Learn more about search behavior and search trends.<\/p>\n","disabled":0,"icon":"fa-user-circle-o","imageClass":"cover","isSection":0,"link":"","name":"Search Behavior","numRecentReplies":1,"order":2,"parentCid":8,"post_count":1793,"slug":"21/search-behavior","topic_count":360,"__imported_original_data__":"{\"_cid\":15,\"_name\":\"Behavior & Demographics\",\"_parentCid\":4000,\"_timestamp\":1296250949000,\"_slug\":\"behavior-demographics\",\"_order\":1,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":1793,"totalTopicCount":360,"children":[],"parent":{"bgColor":"#5dc93a","cid":8,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Dive into research and trends in the search industry.","descriptionParsed":"<p dir=\"auto\">Dive into research and trends in the search industry.<\/p>\n","disabled":0,"icon":"fa-area-chart","imageClass":"cover","isSection":0,"link":"","name":"Research &amp; Trends","numRecentReplies":1,"order":5,"parentCid":0,"post_count":1,"slug":"8/research-trends","topic_count":1,"__imported_original_data__":"{\"_cid\":4000,\"_name\":\"Research & Trends\",\"_order\":4,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":1,"totalTopicCount":1},"value":21,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Search Behavior","depth":1},{"bgColor":"#ff9f2c","cid":23,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss algorithm updates and impacts.","descriptionParsed":"<p dir=\"auto\">Discuss algorithm updates and impacts.<\/p>\n","disabled":0,"icon":"fa-exclamation","imageClass":"cover","isSection":0,"link":"","name":"Algorithm Updates","numRecentReplies":1,"order":3,"parentCid":8,"post_count":8994,"slug":"23/algorithm-updates","topic_count":1943,"__imported_original_data__":"{\"_cid\":17,\"_name\":\"Search Engine Trends\",\"_parentCid\":4000,\"_timestamp\":1296250949000,\"_slug\":\"search-engine-trends\",\"_order\":3,\"_description\":\"\"}","subCategoriesPerPage":10,"image":null,"maxTags":5,"minTags":1,"postQueue":1,"totalPostCount":8994,"totalTopicCount":1943,"children":[],"parent":{"bgColor":"#5dc93a","cid":8,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Dive into research and trends in the search industry.","descriptionParsed":"<p dir=\"auto\">Dive into research and trends in the search industry.<\/p>\n","disabled":0,"icon":"fa-area-chart","imageClass":"cover","isSection":0,"link":"","name":"Research &amp; Trends","numRecentReplies":1,"order":5,"parentCid":0,"post_count":1,"slug":"8/research-trends","topic_count":1,"__imported_original_data__":"{\"_cid\":4000,\"_name\":\"Research & Trends\",\"_order\":4,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":1,"totalTopicCount":1},"value":23,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Algorithm Updates","depth":1},{"bgColor":"#575e66","cid":24,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Dig into white hat and black hat SEO trends.","descriptionParsed":"<p dir=\"auto\">Dig into white hat and black hat SEO trends.<\/p>\n","disabled":0,"icon":"fa-briefcase","imageClass":"cover","isSection":0,"link":"","name":"White Hat &#x2F; Black Hat SEO","numRecentReplies":1,"order":4,"parentCid":8,"post_count":9497,"slug":"24/white-hat-black-hat-seo","topic_count":1907,"__imported_original_data__":"{\"_cid\":18,\"_name\":\"White Hat / Black Hat SEO\",\"_parentCid\":4000,\"_timestamp\":1296250949000,\"_slug\":\"white-hat-black-hat-seo\",\"_order\":4,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":9497,"totalTopicCount":1907,"children":[],"parent":{"bgColor":"#5dc93a","cid":8,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Dive into research and trends in the search industry.","descriptionParsed":"<p dir=\"auto\">Dive into research and trends in the search industry.<\/p>\n","disabled":0,"icon":"fa-area-chart","imageClass":"cover","isSection":0,"link":"","name":"Research &amp; Trends","numRecentReplies":1,"order":5,"parentCid":0,"post_count":1,"slug":"8/research-trends","topic_count":1,"__imported_original_data__":"{\"_cid\":4000,\"_name\":\"Research & Trends\",\"_order\":4,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":1,"totalTopicCount":1},"value":24,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; White Hat &#x2F; Black Hat SEO","depth":1},{"bgColor":"#0a597c","cid":71,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Discuss new SERP trends","descriptionParsed":"<p dir=\"auto\">Discuss new SERP trends<\/p>\n","disabled":0,"icon":"fa-wrench","imageClass":"cover","isSection":0,"link":"","name":"Other SEO Tools","numRecentReplies":1,"order":5,"parentCid":8,"post_count":104,"slug":"71/other-seo-tools","subCategoriesPerPage":10,"topic_count":28,"image":null,"maxTags":5,"minTags":1,"postQueue":1,"totalPostCount":104,"totalTopicCount":28,"children":[],"parent":{"bgColor":"#5dc93a","cid":8,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Dive into research and trends in the search industry.","descriptionParsed":"<p dir=\"auto\">Dive into research and trends in the search industry.<\/p>\n","disabled":0,"icon":"fa-area-chart","imageClass":"cover","isSection":0,"link":"","name":"Research &amp; Trends","numRecentReplies":1,"order":5,"parentCid":0,"post_count":1,"slug":"8/research-trends","topic_count":1,"__imported_original_data__":"{\"_cid\":4000,\"_name\":\"Research & Trends\",\"_order\":4,\"_timestamp\":1296250949000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":1,"totalTopicCount":1},"value":71,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Other SEO Tools","depth":1}],"value":8,"level":"","text":"Research &amp; Trends","depth":0},{"bgColor":"#575e66","cid":4,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Connect on product support and feature requests.","descriptionParsed":"<p dir=\"auto\">Connect on product support and feature requests.<\/p>\n","disabled":0,"icon":"fa-comment","imageClass":"cover","isSection":1,"link":"","name":"Support","numRecentReplies":1,"order":6,"parentCid":0,"post_count":43,"slug":"4/support","topic_count":15,"__imported_original_data__":"{\"_cid\":1000,\"_name\":\"Help with Moz Products & Tools\",\"_order\":1,\"_timestamp\":1369824092000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":2955,"totalTopicCount":765,"children":[{"bgColor":"#fc4949","cid":49,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Find expert assistance to help you troubleshoot technical issues with the Moz tools.","descriptionParsed":"<p dir=\"auto\">Find expert assistance to help you troubleshoot technical issues with the Moz tools.<\/p>\n","disabled":0,"icon":"fa-comments-o","imageClass":"cover","isSection":0,"link":"","name":"Product Support","numRecentReplies":1,"order":1,"parentCid":4,"post_count":2320,"slug":"49/product-support","topic_count":600,"__imported_original_data__":"{\"_cid\":47,\"_name\":\"Technical Support\",\"_parentCid\":1000,\"_timestamp\":1369824092000,\"_slug\":\"technical-support\",\"_order\":10,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":2320,"totalTopicCount":600,"children":[],"parent":{"bgColor":"#575e66","cid":4,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Connect on product support and feature requests.","descriptionParsed":"<p dir=\"auto\">Connect on product support and feature requests.<\/p>\n","disabled":0,"icon":"fa-comment","imageClass":"cover","isSection":1,"link":"","name":"Support","numRecentReplies":1,"order":6,"parentCid":0,"post_count":43,"slug":"4/support","topic_count":15,"__imported_original_data__":"{\"_cid\":1000,\"_name\":\"Help with Moz Products & Tools\",\"_order\":1,\"_timestamp\":1369824092000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":43,"totalTopicCount":15},"value":49,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Product Support","depth":1},{"bgColor":"#5ec93a","cid":63,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Let us know about features and functionality that you’d like to see in the Moz tools.","descriptionParsed":"<p dir=\"auto\">Let us know about features and functionality that you’d like to see in the Moz tools.<\/p>\n","disabled":0,"icon":"fa-lightbulb-o","imageClass":"cover","isSection":0,"link":"","name":"Feature Requests","numRecentReplies":1,"order":2,"parentCid":4,"post_count":592,"slug":"63/feature-requests","topic_count":150,"__imported_original_data__":"{\"_cid\":83,\"_name\":\"Feature Requests\",\"_parentCid\":1000,\"_timestamp\":1429040368000,\"_slug\":\"feature-requests\",\"_order\":11,\"_description\":\"\"}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":592,"totalTopicCount":150,"children":[],"parent":{"bgColor":"#575e66","cid":4,"class":"col-md-3 col-xs-6","color":"#FFFFFF","description":"Connect on product support and feature requests.","descriptionParsed":"<p dir=\"auto\">Connect on product support and feature requests.<\/p>\n","disabled":0,"icon":"fa-comment","imageClass":"cover","isSection":1,"link":"","name":"Support","numRecentReplies":1,"order":6,"parentCid":0,"post_count":43,"slug":"4/support","topic_count":15,"__imported_original_data__":"{\"_cid\":1000,\"_name\":\"Help with Moz Products & Tools\",\"_order\":1,\"_timestamp\":1369824092000,\"_description\":\"\",\"_parentCid\":null}","subCategoriesPerPage":10,"minTags":1,"maxTags":5,"postQueue":1,"totalPostCount":43,"totalTopicCount":15},"value":63,"level":"&nbsp;&nbsp;&nbsp;&nbsp;","text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Feature Requests","depth":1}],"value":4,"level":"","text":"Support","depth":0}],"categoriesList":[{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Affiliate Marketing","value":33,"name":"Affiliate Marketing","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Algorithm Updates","value":23,"name":"Algorithm Updates","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; API","value":56,"name":"API","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Branding","value":31,"name":"Branding","isSection":0},{"text":"Community","value":3,"name":"Community","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Competitive Research","value":19,"name":"Competitive Research","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Content Development","value":10,"name":"Content Development","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Conversion Rate Optimization","value":34,"name":"Conversion Rate Optimization","isSection":0},{"text":"Digital Marketing","value":7,"name":"Digital Marketing","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Feature Requests","value":63,"name":"Feature Requests","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Getting Started","value":53,"name":"Getting Started","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Image &amp; Video Optimization","value":14,"name":"Image &amp; Video Optimization","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&bull; Industry Events","value":40,"name":"Industry Events","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Industry News","value":44,"name":"Industry News","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Intermediate &amp; Advanced SEO","value":16,"name":"Intermediate &amp; Advanced SEO","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; International SEO","value":22,"name":"International SEO","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Jobs and Opportunities","value":43,"name":"Jobs and Opportunities","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&bull; Keyword Explorer","value":64,"name":"Keyword Explorer","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Keyword Research","value":12,"name":"Keyword Research","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Link Building","value":13,"name":"Link Building","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&bull; Link Explorer","value":55,"name":"Link Explorer","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&bull; Local Listings","value":59,"name":"Local Listings","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Local SEO","value":5,"name":"Local SEO","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&bull; Local Website Optimization","value":58,"name":"Local Website Optimization","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Moz Bar","value":52,"name":"Moz Bar","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Moz Local","value":54,"name":"Moz Local","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Moz News","value":48,"name":"Moz News","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Moz Pro","value":46,"name":"Moz Pro","isSection":0},{"text":"Moz Tools","value":47,"name":"Moz Tools","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; On-Page Optimization","value":11,"name":"On-Page Optimization","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Other SEO Tools","value":71,"name":"Other SEO Tools","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Paid Search Marketing","value":29,"name":"Paid Search Marketing","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Product Support","value":49,"name":"Product Support","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Reporting &amp; Analytics","value":6,"name":"Reporting &amp; Analytics","isSection":0},{"text":"Research &amp; Trends","value":8,"name":"Research &amp; Trends","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&bull; Reviews and Ratings","value":60,"name":"Reviews and Ratings","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Search Behavior","value":21,"name":"Search Behavior","isSection":0},{"text":"SEO Tactics","value":9,"name":"SEO Tactics","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; SERP Trends","value":26,"name":"SERP Trends","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Social Media","value":27,"name":"Social Media","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Technical SEO","value":15,"name":"Technical SEO","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; Web Design","value":25,"name":"Web Design","isSection":0},{"text":"&nbsp;&nbsp;&nbsp;&nbsp;&bull; White Hat &#x2F; Black Hat SEO","value":24,"name":"White Hat &#x2F; Black Hat SEO","isSection":0}],"_header":{"tags":{"meta":[{"name":"viewport","content":"width&#x3D;device-width, initial-scale&#x3D;1.0"},{"name":"content-type","content":"text/html; charset=UTF-8","noEscape":true},{"name":"apple-mobile-web-app-capable","content":"yes"},{"name":"mobile-web-app-capable","content":"yes"},{"property":"og:site_name","content":"Moz"},{"name":"msapplication-badge","content":"frequency=30; polling-uri=https://moz.com/community/q/sitemap.xml","noEscape":true},{"name":"theme-color","content":"#ffffff"},{"name":"msapplication-square150x150logo","content":"/community/q/assets/uploads/system/site-logo.png","noEscape":true},{"name":"title","content":"Pages with excessive number of links"},{"name":"description","content":"Pre 2013 it was bad practice to have in excess of 100 links per page, google technical guideline.  Many SEO tools still use it as a warning bell. However Matt Cutts from google - I recall a few years ago - came out and categorically said it is NOT bad pra..."},{"property":"og:title","content":"Pages with excessive number of links"},{"property":"og:description","content":"Pre 2013 it was bad practice to have in excess of 100 links per page, google technical guideline.  Many SEO tools still use it as a warning bell. However Matt Cutts from google - I recall a few years ago - came out and categorically said it is NOT bad pra..."},{"property":"og:type","content":"article"},{"property":"article:published_time","content":"2016-02-17T07:10:59.000Z"},{"property":"article:modified_time","content":"2016-02-17T08:48:15.000Z"},{"property":"article:section","content":"Intermediate &amp;amp; Advanced SEO"},{"property":"og:image","content":"https://moz.com/community/q/assets/uploads/profile/77292-profileavatar-1619582671334.png","noEscape":true},{"property":"og:image:url","content":"https://moz.com/community/q/assets/uploads/profile/77292-profileavatar-1619582671334.png","noEscape":true},{"property":"og:image","content":"https://moz.com/community/q/assets/uploads/system/og-image.jpg","noEscape":true},{"property":"og:image:url","content":"https://moz.com/community/q/assets/uploads/system/og-image.jpg","noEscape":true},{"property":"og:image:width","content":"1200"},{"property":"og:image:height","content":"630"},{"content":"https://moz.com/community/q/topic/58032/pages-with-excessive-number-of-links/3","property":"og:url"}],"link":[{"rel":"icon","type":"image/x-icon","href":"/community/q/assets/uploads/system/favicon.ico?v&#x3D;4jds23d1a2r"},{"rel":"manifest","href":"/community/q/manifest.webmanifest","crossorigin":"use-credentials"},{"rel":"search","type":"application/opensearchdescription+xml","title":"Moz","href":"/community/q/osd.xml"},{"rel":"apple-touch-icon","href":"/community/q/assets/uploads/system/touchicon-orig.png"},{"rel":"icon","sizes":"36x36","href":"/community/q/assets/uploads/system/touchicon-36.png"},{"rel":"icon","sizes":"48x48","href":"/community/q/assets/uploads/system/touchicon-48.png"},{"rel":"icon","sizes":"72x72","href":"/community/q/assets/uploads/system/touchicon-72.png"},{"rel":"icon","sizes":"96x96","href":"/community/q/assets/uploads/system/touchicon-96.png"},{"rel":"icon","sizes":"144x144","href":"/community/q/assets/uploads/system/touchicon-144.png"},{"rel":"icon","sizes":"192x192","href":"/community/q/assets/uploads/system/touchicon-192.png"},{"rel":"prefetch","href":"/community/q/assets/src/modules/composer.js?v&#x3D;4jds23d1a2r"},{"rel":"prefetch","href":"/community/q/assets/src/modules/composer/uploads.js?v&#x3D;4jds23d1a2r"},{"rel":"prefetch","href":"/community/q/assets/src/modules/composer/drafts.js?v&#x3D;4jds23d1a2r"},{"rel":"prefetch","href":"/community/q/assets/src/modules/composer/tags.js?v&#x3D;4jds23d1a2r"},{"rel":"prefetch","href":"/community/q/assets/src/modules/composer/categoryList.js?v&#x3D;4jds23d1a2r"},{"rel":"prefetch","href":"/community/q/assets/src/modules/composer/resize.js?v&#x3D;4jds23d1a2r"},{"rel":"prefetch","href":"/community/q/assets/src/modules/composer/autocomplete.js?v&#x3D;4jds23d1a2r"},{"rel":"prefetch","href":"/community/q/assets/templates/composer.tpl?v&#x3D;4jds23d1a2r"},{"rel":"prefetch","href":"/community/q/assets/language/en-US/topic.json?v&#x3D;4jds23d1a2r"},{"rel":"prefetch","href":"/community/q/assets/language/en-US/modules.json?v&#x3D;4jds23d1a2r"},{"rel":"prefetch","href":"/community/q/assets/language/en-US/tags.json?v&#x3D;4jds23d1a2r"},{"rel":"prefetch stylesheet","type":"","href":"/community/q/assets/plugins/nodebb-plugin-markdown/styles/default.css"},{"rel":"prefetch","href":"/community/q/assets/language/en-US/markdown.json?v&#x3D;4jds23d1a2r"},{"rel":"stylesheet","href":"https://moz.com/community/q/assets/plugins/nodebb-plugin-emoji/emoji/styles.css?v&#x3D;4jds23d1a2r"},{"rel":"canonical","href":"https://moz.com/community/q/topic/58032/pages-with-excessive-number-of-links"},{"rel":"up","href":"https://moz.com/community/q/category/16/intermediate-advanced-seo"}]}},"widgets":{"sidebar":[{"html":"<div class=\"side-box\"><div class=\"panel-heading\"><h4>Explore more categories<\/h4><\/div><div class=\"panel-body\">\n<ul class=\"categories-list\">\n\t<li>\n\t\t\n\t\t<h4><a href=\"/community/q/category/47/moz-tools\">Moz Tools<\/a><\/h4>\n\t\t\n\t\t<p><p dir=\"auto\">Chat with the community about the Moz tools.<\/p>\n<\/p>\n\t<\/li>\n<\/ul>\n\n<ul class=\"categories-list\">\n\t<li>\n\t\t\n\t\t<h4><a href=\"/community/q/category/9/seo-tactics\">SEO Tactics<\/a><\/h4>\n\t\t\n\t\t<p><p dir=\"auto\">Discuss the SEO process with fellow marketers<\/p>\n<\/p>\n\t<\/li>\n<\/ul>\n\n<ul class=\"categories-list\">\n\t<li>\n\t\t\n\t\t<h4><a href=\"/community/q/category/3/community\">Community<\/a><\/h4>\n\t\t\n\t\t<p><p dir=\"auto\">Discuss industry events, jobs, and news!<\/p>\n<\/p>\n\t<\/li>\n<\/ul>\n\n<ul class=\"categories-list\">\n\t<li>\n\t\t\n\t\t<h4><a href=\"/community/q/category/7/digital-marketing\">Digital Marketing<\/a><\/h4>\n\t\t\n\t\t<p><p dir=\"auto\">Chat about tactics outside of SEO<\/p>\n<\/p>\n\t<\/li>\n<\/ul>\n\n<ul class=\"categories-list\">\n\t<li>\n\t\t\n\t\t<h4><a href=\"/community/q/category/8/research-trends\">Research &amp; Trends<\/a><\/h4>\n\t\t\n\t\t<p><p dir=\"auto\">Dive into research and trends in the search industry.<\/p>\n<\/p>\n\t<\/li>\n<\/ul>\n\n<ul class=\"categories-list\">\n\t<li>\n\t\t\n\t\t<h4><a href=\"/community/q/category/4/support\">Support<\/a><\/h4>\n\t\t\n\t\t<p><p dir=\"auto\">Connect on product support and feature requests.<\/p>\n<\/p>\n\t<\/li>\n<\/ul>\n\n<ul class=\"categories-list\">\n\t<li>\n\t\t\n\t\t<h4><a href=\"https:&#x2F;&#x2F;moz.com&#x2F;community&#x2F;q&#x2F;categories\">See all categories<\/a><\/h4>\n\t\t\n\t\t<p><\/p>\n\t<\/li>\n<\/ul>\n<\/div><\/div>"},{"html":"<div class=\"topics-list\">\n\t<h4>Related Questions<\/h4>\n\t<div class=\"category\">\n\t\t<ul component=\"category\" class=\"topic-list\" itemscope itemtype=\"http://www.schema.org/ItemList\" data-nextstart=\"\" data-set=\"\">\n\t<meta itemprop=\"itemListOrder\" content=\"descending\">\n\t\n\t<li component=\"category/topic\" class=\"clearfix category-item locked unread \" data-tid=\"63188\" data-index=\"0\" data-cid=\"16\" itemprop=\"itemListElement\" itemscope itemtype=\"https://schema.org/ListItem\">\n\t\t<link itemprop=\"url\" content=\"/community/q/topic/63188/link-types-for-link-building\" />\n\t\t<meta itemprop=\"name\" content=\"Link Types For Link Building\" />\n\t\t<meta itemprop=\"itemListOrder\" content=\"descending\" />\n\t\t<meta itemprop=\"position\" content=\"1\" />\n\t\t<a id=\"0\" data-index=\"0\" component=\"topic/anchor\"><\/a>\n\n\t\t<div class=\"content\">\n\t\t\t<div class=\"avatar pull-left\">\n\t\t\t\t\n\n\t\t\t\t\n\t\t\t\t<a href=\"/community/q/user/spyaccounts14\" class=\"pull-left\">\n\t\t\t\t\t\n\t\t\t\t\t<img class=\"avatar not-responsive avatar-rounded\" alt=\"spyaccounts14\" title=\"spyaccounts14\" data-uid=\"132358\" loading=\"lazy\" component=\"avatar/icon\" src=\"https://moz.com/avatar/large/8/s.png\"><\/img>\n\t\t\t\t\t\n\t\t\t\t<\/a>\n\t\t\t\t\n\t\t\t<\/div>\n\n\t\t\t<h3 component=\"topic/header\" class=\"title\">\n\t\t\t\t<i component=\"topic/pinned\" class=\"fa fa-thumb-tack hide\" title=\"Pinned\"><\/i>\n\t\t\t\t<i component=\"topic/locked\" class=\"fa fa-lock \" title=\"Locked\"><\/i>\n\t\t\t\t<i component=\"topic/moved\" class=\"fa fa-arrow-circle-right hide\" title=\"Moved\"><\/i>\n\t\t\t\t\n\n\t\t\t\t\n\t\t\t\t<a href=\"/community/q/topic/63188/link-types-for-link-building/6\" itemprop=\"url\">Link Types For Link Building<\/a><br />\n\t\t\t\t\n\t\t\t<\/h3>\n\n\t\t\t\n\n\t\t\t<div class=\"category-content\">\n\t\t\t\t\n\t\t\t\t<p dir=\"auto\">Hi i have a SEO agency we work with who are building quality guest post links for us, however they are also building forum, profile, blog comments <br />\nand directory based links.\n60% of their links they are building are high quality, relevant guest posts while the other 40% are the other link types.\nThe 40% seem to be relevant directories, forums, blog comments, etc.\nThey said they build other link types because it diversifies the link building and profile rather then just building high quality guest posts.\nAs just building one link type can leave a footprint.\nWhat are your thoughts on this?\nCheers.\n<\/p>\n\t\t\t\t\n\t\t\t\t\n\t\t\t\t<small class=\"category-name\">\n\t\t\t\t\t<a href=\"/community/q/category/16/intermediate-advanced-seo\"><span class=\"fa-stack fa-lg\" style=\"background-color: #fc4949; color: #FFFFFF;\"><i style=\"color:#FFFFFF;\" class=\"fa fa-graduation-cap fa-stack-1x\"><\/i><\/span> Intermediate &amp; Advanced SEO<\/a> |\n\t\t\t\t<\/small>\n\t\t\t\t\n\n\t\t\t\t<small>\n\t\t\t\t\t\n\t\t\t\t\t<span class=\"timeago\" title=\"2017-05-03T12:19:21.000Z\"><\/span>\n\t\t\t\t\t| <a href=\"/community/q/user/spyaccounts14\">spyaccounts14<\/a>\n\t\t\t\t\t\n\t\t\t\t<\/small>\n\t\t\t<\/div>\n\n\t\t\t\n\t\t\t<div class=\"votes\" title=\"Votes\">\n\t\t\t\t<i class=\"fa fa-thumbs-up\"><\/i> <span class=\"human-readable-number\" title=\"0\">0<\/span>\n\t\t\t<\/div>\n\t\t\t\n\t\t<\/div>\n\t<\/li>\n\t\n\t<li component=\"category/topic\" class=\"clearfix category-item locked unread \" data-tid=\"58722\" data-index=\"1\" data-cid=\"16\" itemprop=\"itemListElement\" itemscope itemtype=\"https://schema.org/ListItem\">\n\t\t<link itemprop=\"url\" content=\"/community/q/topic/58722/seo-implication-of-adding-large-number-of-new-product-pages\" />\n\t\t<meta itemprop=\"name\" content=\"SEO implication of adding large number of new product pages\" />\n\t\t<meta itemprop=\"itemListOrder\" content=\"descending\" />\n\t\t<meta itemprop=\"position\" content=\"2\" />\n\t\t<a id=\"1\" data-index=\"1\" component=\"topic/anchor\"><\/a>\n\n\t\t<div class=\"content\">\n\t\t\t<div class=\"avatar pull-left\">\n\t\t\t\t\n\n\t\t\t\t\n\t\t\t\t<a href=\"/community/q/user/dhs_sh\" class=\"pull-left\">\n\t\t\t\t\t\n\t\t\t\t\t<img class=\"avatar not-responsive avatar-rounded\" alt=\"DHS_SH\" title=\"DHS_SH\" data-uid=\"39447\" loading=\"lazy\" component=\"avatar/icon\" src=\"https://moz.com/avatar/large/7/d.png\"><\/img>\n\t\t\t\t\t\n\t\t\t\t<\/a>\n\t\t\t\t\n\t\t\t<\/div>\n\n\t\t\t<h3 component=\"topic/header\" class=\"title\">\n\t\t\t\t<i component=\"topic/pinned\" class=\"fa fa-thumb-tack hide\" title=\"Pinned\"><\/i>\n\t\t\t\t<i component=\"topic/locked\" class=\"fa fa-lock \" title=\"Locked\"><\/i>\n\t\t\t\t<i component=\"topic/moved\" class=\"fa fa-arrow-circle-right hide\" title=\"Moved\"><\/i>\n\t\t\t\t\n\n\t\t\t\t\n\t\t\t\t<a href=\"/community/q/topic/58722/seo-implication-of-adding-large-number-of-new-product-pages/4\" itemprop=\"url\">SEO implication of adding large number of new product pages<\/a><br />\n\t\t\t\t\n\t\t\t<\/h3>\n\n\t\t\t\n\n\t\t\t<div class=\"category-content\">\n\t\t\t\t\n\t\t\t\t<p dir=\"auto\">If I have an eCommerce website containing 10,000 product pages and then I add 10,000 new product pages using a bulk upload (with limited/basic but unique content), does this pose any SEO risk?\nI am obviously aware of the risks of adding a large number of low quality content to the website, which is not the case here, however what I am trying to ascertain is whether simply doubling the number of pages in itself causes any risk to our SEO efforts? Does it flag to the Search Engines that something \"spammy\" is happening (even if its not)\n<\/p>\n\t\t\t\t\n\t\t\t\t\n\t\t\t\t<small class=\"category-name\">\n\t\t\t\t\t<a href=\"/community/q/category/16/intermediate-advanced-seo\"><span class=\"fa-stack fa-lg\" style=\"background-color: #fc4949; color: #FFFFFF;\"><i style=\"color:#FFFFFF;\" class=\"fa fa-graduation-cap fa-stack-1x\"><\/i><\/span> Intermediate &amp; Advanced SEO<\/a> |\n\t\t\t\t<\/small>\n\t\t\t\t\n\n\t\t\t\t<small>\n\t\t\t\t\t\n\t\t\t\t\t<span class=\"timeago\" title=\"2016-04-07T09:46:55.000Z\"><\/span>\n\t\t\t\t\t| <a href=\"/community/q/user/dhs_sh\">DHS_SH<\/a>\n\t\t\t\t\t\n\t\t\t\t<\/small>\n\t\t\t<\/div>\n\n\t\t\t\n\t\t\t<div class=\"votes\" title=\"Votes\">\n\t\t\t\t<i class=\"fa fa-thumbs-up\"><\/i> <span class=\"human-readable-number\" title=\"0\">0<\/span>\n\t\t\t<\/div>\n\t\t\t\n\t\t<\/div>\n\t<\/li>\n\t\n\t<li component=\"category/topic\" class=\"clearfix category-item locked unread \" data-tid=\"55772\" data-index=\"2\" data-cid=\"16\" itemprop=\"itemListElement\" itemscope itemtype=\"https://schema.org/ListItem\">\n\t\t<link itemprop=\"url\" content=\"/community/q/topic/55772/what-to-do-when-your-home-page-an-index-for-a-series-of-pages\" />\n\t\t<meta itemprop=\"name\" content=\"What to do when your home page an index for a series of pages.\" />\n\t\t<meta itemprop=\"itemListOrder\" content=\"descending\" />\n\t\t<meta itemprop=\"position\" content=\"3\" />\n\t\t<a id=\"2\" data-index=\"2\" component=\"topic/anchor\"><\/a>\n\n\t\t<div class=\"content\">\n\t\t\t<div class=\"avatar pull-left\">\n\t\t\t\t\n\n\t\t\t\t\n\t\t\t\t<a href=\"/community/q/user/velocitywebsites\" class=\"pull-left\">\n\t\t\t\t\t\n\t\t\t\t\t<img class=\"avatar not-responsive avatar-rounded\" alt=\"VelocityWebsites\" title=\"VelocityWebsites\" data-uid=\"91079\" loading=\"lazy\" component=\"avatar/picture\" src=\"/community/q/assets/uploads/profile/91079-profileavatar-1619583208014.png\" style=\"width: 46px; height: 46px; line-height: 46px; font-size: 2.875rem;\" />\n\t\t\t\t\t\n\t\t\t\t<\/a>\n\t\t\t\t\n\t\t\t<\/div>\n\n\t\t\t<h3 component=\"topic/header\" class=\"title\">\n\t\t\t\t<i component=\"topic/pinned\" class=\"fa fa-thumb-tack hide\" title=\"Pinned\"><\/i>\n\t\t\t\t<i component=\"topic/locked\" class=\"fa fa-lock \" title=\"Locked\"><\/i>\n\t\t\t\t<i component=\"topic/moved\" class=\"fa fa-arrow-circle-right hide\" title=\"Moved\"><\/i>\n\t\t\t\t\n\n\t\t\t\t\n\t\t\t\t<a href=\"/community/q/topic/55772/what-to-do-when-your-home-page-an-index-for-a-series-of-pages/9\" itemprop=\"url\">What to do when your home page an index for a series of pages.<\/a><br />\n\t\t\t\t\n\t\t\t<\/h3>\n\n\t\t\t\n\n\t\t\t<div class=\"category-content\">\n\t\t\t\t\n\t\t\t\t<p dir=\"auto\">I have created an index stack.  My home page is http://www.southernwhitewater.com\nThe home page is the index itself and the 1st page http://www.southernwhitewater.com/nz-adventure-tours-whitewater-river-rafting-hunting-fishing\nMy home page (if your look at it through moz bat for chrome bar} incorporates all the pages in the index. Is this Bad?  I would prefer to index each page separately.  As per my site index in the footer\nWhat is the best way to optimize all these pages individually and still have the customers arrive at the top to a picture.  rel= canonical?\nAny help would be great!!\nhttp://www.southernwhitewater.com\n<\/p>\n\t\t\t\t\n\t\t\t\t\n\t\t\t\t<small class=\"category-name\">\n\t\t\t\t\t<a href=\"/community/q/category/16/intermediate-advanced-seo\"><span class=\"fa-stack fa-lg\" style=\"background-color: #fc4949; color: #FFFFFF;\"><i style=\"color:#FFFFFF;\" class=\"fa fa-graduation-cap fa-stack-1x\"><\/i><\/span> Intermediate &amp; Advanced SEO<\/a> |\n\t\t\t\t<\/small>\n\t\t\t\t\n\n\t\t\t\t<small>\n\t\t\t\t\t\n\t\t\t\t\t<span class=\"timeago\" title=\"2015-09-20T05:44:50.000Z\"><\/span>\n\t\t\t\t\t| <a href=\"/community/q/user/velocitywebsites\">VelocityWebsites<\/a>\n\t\t\t\t\t\n\t\t\t\t<\/small>\n\t\t\t<\/div>\n\n\t\t\t\n\t\t\t<div class=\"votes\" title=\"Votes\">\n\t\t\t\t<i class=\"fa fa-thumbs-up\"><\/i> <span class=\"human-readable-number\" title=\"0\">0<\/span>\n\t\t\t<\/div>\n\t\t\t\n\t\t<\/div>\n\t<\/li>\n\t\n\t<li component=\"category/topic\" class=\"clearfix category-item locked unread \" data-tid=\"55351\" data-index=\"3\" data-cid=\"16\" itemprop=\"itemListElement\" itemscope itemtype=\"https://schema.org/ListItem\">\n\t\t<link itemprop=\"url\" content=\"/community/q/topic/55351/i-ve-got-duplicate-pages-for-example-blog-page-2-is-the-same-as-author-admin-page-2-is-this-something-i-should-just-ignore-or-should-i-create-the-author-admin-page2-and-then-301-redirect\" />\n\t\t<meta itemprop=\"name\" content=\"I&#x27;ve got duplicate pages. For example, blog&#x2F;page&#x2F;2 is the same as author&#x2F;admin&#x2F;page&#x2F;2&#x5C;. Is this something I should just ignore, or should I create the author&#x2F;admin&#x2F;page2 and then 301 redirect?\" />\n\t\t<meta itemprop=\"itemListOrder\" content=\"descending\" />\n\t\t<meta itemprop=\"position\" content=\"4\" />\n\t\t<a id=\"3\" data-index=\"3\" component=\"topic/anchor\"><\/a>\n\n\t\t<div class=\"content\">\n\t\t\t<div class=\"avatar pull-left\">\n\t\t\t\t\n\n\t\t\t\t\n\t\t\t\t<a href=\"/community/q/user/shift-inc\" class=\"pull-left\">\n\t\t\t\t\t\n\t\t\t\t\t<img class=\"avatar not-responsive avatar-rounded\" alt=\"shift-inc\" title=\"shift-inc\" data-uid=\"71696\" loading=\"lazy\" component=\"avatar/picture\" src=\"/community/q/assets/uploads/profile/71696-profileavatar-1619583200464.png\" style=\"width: 46px; height: 46px; line-height: 46px; font-size: 2.875rem;\" />\n\t\t\t\t\t\n\t\t\t\t<\/a>\n\t\t\t\t\n\t\t\t<\/div>\n\n\t\t\t<h3 component=\"topic/header\" class=\"title\">\n\t\t\t\t<i component=\"topic/pinned\" class=\"fa fa-thumb-tack hide\" title=\"Pinned\"><\/i>\n\t\t\t\t<i component=\"topic/locked\" class=\"fa fa-lock \" title=\"Locked\"><\/i>\n\t\t\t\t<i component=\"topic/moved\" class=\"fa fa-arrow-circle-right hide\" title=\"Moved\"><\/i>\n\t\t\t\t\n\n\t\t\t\t\n\t\t\t\t<a href=\"/community/q/topic/55351/i-ve-got-duplicate-pages-for-example-blog-page-2-is-the-same-as-author-admin-page-2-is-this-something-i-should-just-ignore-or-should-i-create-the-author-admin-page2-and-then-301-redirect/7\" itemprop=\"url\">I&#x27;ve got duplicate pages. For example, blog&#x2F;page&#x2F;2 is the same as author&#x2F;admin&#x2F;page&#x2F;2&#x5C;. Is this something I should just ignore, or should I create the author&#x2F;admin&#x2F;page2 and then 301 redirect?<\/a><br />\n\t\t\t\t\n\t\t\t<\/h3>\n\n\t\t\t\n\n\t\t\t<div class=\"category-content\">\n\t\t\t\t\n\t\t\t\t<p dir=\"auto\">I'm going through the crawl report and it says I've got duplicate pages. For example, blog/page/2 is the same as   author/admin/page/2/  Now, the author/admin/page/2 I can't even find in WordPress, but it is the same thing as blog/page/2 nonetheless. Is this something I should just ignore, or should I create the author/admin/page2 and then 301 redirect it to blog/page/2?\n<\/p>\n\t\t\t\t\n\t\t\t\t\n\t\t\t\t<small class=\"category-name\">\n\t\t\t\t\t<a href=\"/community/q/category/16/intermediate-advanced-seo\"><span class=\"fa-stack fa-lg\" style=\"background-color: #fc4949; color: #FFFFFF;\"><i style=\"color:#FFFFFF;\" class=\"fa fa-graduation-cap fa-stack-1x\"><\/i><\/span> Intermediate &amp; Advanced SEO<\/a> |\n\t\t\t\t<\/small>\n\t\t\t\t\n\n\t\t\t\t<small>\n\t\t\t\t\t\n\t\t\t\t\t<span class=\"timeago\" title=\"2015-08-21T14:28:04.000Z\"><\/span>\n\t\t\t\t\t| <a href=\"/community/q/user/shift-inc\">shift-inc<\/a>\n\t\t\t\t\t\n\t\t\t\t<\/small>\n\t\t\t<\/div>\n\n\t\t\t\n\t\t\t<div class=\"votes\" title=\"Votes\">\n\t\t\t\t<i class=\"fa fa-thumbs-up\"><\/i> <span class=\"human-readable-number\" title=\"0\">0<\/span>\n\t\t\t<\/div>\n\t\t\t\n\t\t<\/div>\n\t<\/li>\n\t\n\t<li component=\"category/topic\" class=\"clearfix category-item locked unread \" data-tid=\"54568\" data-index=\"4\" data-cid=\"16\" itemprop=\"itemListElement\" itemscope itemtype=\"https://schema.org/ListItem\">\n\t\t<link itemprop=\"url\" content=\"/community/q/topic/54568/on-1-of-our-sites-we-have-our-company-name-in-the-h1-on-our-other-site-we-have-the-page-title-in-our-h1-does-anyone-have-any-advise-about-the-best-information-to-have-in-the-h1-h2-and-page-tile\" />\n\t\t<meta itemprop=\"name\" content=\"On 1 of our sites we have our Company name in the H1 on our other site we have the page title in our H1 - does anyone have any advise about the best information to have in the H1, H2 and Page Tile\" />\n\t\t<meta itemprop=\"itemListOrder\" content=\"descending\" />\n\t\t<meta itemprop=\"position\" content=\"5\" />\n\t\t<a id=\"4\" data-index=\"4\" component=\"topic/anchor\"><\/a>\n\n\t\t<div class=\"content\">\n\t\t\t<div class=\"avatar pull-left\">\n\t\t\t\t\n\n\t\t\t\t\n\t\t\t\t<a href=\"/community/q/user/costumed\" class=\"pull-left\">\n\t\t\t\t\t\n\t\t\t\t\t<img class=\"avatar not-responsive avatar-rounded\" alt=\"CostumeD\" title=\"CostumeD\" data-uid=\"83039\" loading=\"lazy\" component=\"avatar/icon\" src=\"https://moz.com/avatar/large/9/c.png\"><\/img>\n\t\t\t\t\t\n\t\t\t\t<\/a>\n\t\t\t\t\n\t\t\t<\/div>\n\n\t\t\t<h3 component=\"topic/header\" class=\"title\">\n\t\t\t\t<i component=\"topic/pinned\" class=\"fa fa-thumb-tack hide\" title=\"Pinned\"><\/i>\n\t\t\t\t<i component=\"topic/locked\" class=\"fa fa-lock \" title=\"Locked\"><\/i>\n\t\t\t\t<i component=\"topic/moved\" class=\"fa fa-arrow-circle-right hide\" title=\"Moved\"><\/i>\n\t\t\t\t\n\n\t\t\t\t\n\t\t\t\t<a href=\"/community/q/topic/54568/on-1-of-our-sites-we-have-our-company-name-in-the-h1-on-our-other-site-we-have-the-page-title-in-our-h1-does-anyone-have-any-advise-about-the-best-information-to-have-in-the-h1-h2-and-page-tile/7\" itemprop=\"url\">On 1 of our sites we have our Company name in the H1 on our other site we have the page title in our H1 - does anyone have any advise about the best information to have in the H1, H2 and Page Tile<\/a><br />\n\t\t\t\t\n\t\t\t<\/h3>\n\n\t\t\t\n\n\t\t\t<div class=\"category-content\">\n\t\t\t\t\n\t\t\t\t<p dir=\"auto\">We have 2 sites that have been set up slightly differently. On 1 site we have the Company name in the H1 and the product name in the page title and H2. On the other site we have the Product name in the H1 and no H2.\nDoes anyone have any advise about the best information to have in the H1 and H2\n<\/p>\n\t\t\t\t\n\t\t\t\t\n\t\t\t\t<small class=\"category-name\">\n\t\t\t\t\t<a href=\"/community/q/category/16/intermediate-advanced-seo\"><span class=\"fa-stack fa-lg\" style=\"background-color: #fc4949; color: #FFFFFF;\"><i style=\"color:#FFFFFF;\" class=\"fa fa-graduation-cap fa-stack-1x\"><\/i><\/span> Intermediate &amp; Advanced SEO<\/a> |\n\t\t\t\t<\/small>\n\t\t\t\t\n\n\t\t\t\t<small>\n\t\t\t\t\t\n\t\t\t\t\t<span class=\"timeago\" title=\"2015-07-08T10:13:17.000Z\"><\/span>\n\t\t\t\t\t| <a href=\"/community/q/user/costumed\">CostumeD<\/a>\n\t\t\t\t\t\n\t\t\t\t<\/small>\n\t\t\t<\/div>\n\n\t\t\t\n\t\t\t<div class=\"votes\" title=\"Votes\">\n\t\t\t\t<i class=\"fa fa-thumbs-up\"><\/i> <span class=\"human-readable-number\" title=\"0\">0<\/span>\n\t\t\t<\/div>\n\t\t\t\n\t\t<\/div>\n\t<\/li>\n\t\n\t<li component=\"category/topic\" class=\"clearfix category-item locked unread \" data-tid=\"38135\" data-index=\"5\" data-cid=\"16\" itemprop=\"itemListElement\" itemscope itemtype=\"https://schema.org/ListItem\">\n\t\t<link itemprop=\"url\" content=\"/community/q/topic/38135/varying-internal-link-anchor-text-with-each-new-page-load\" />\n\t\t<meta itemprop=\"name\" content=\"Varying Internal Link Anchor Text with Each New Page Load\" />\n\t\t<meta itemprop=\"itemListOrder\" content=\"descending\" />\n\t\t<meta itemprop=\"position\" content=\"6\" />\n\t\t<a id=\"5\" data-index=\"5\" component=\"topic/anchor\"><\/a>\n\n\t\t<div class=\"content\">\n\t\t\t<div class=\"avatar pull-left\">\n\t\t\t\t\n\n\t\t\t\t\n\t\t\t\t<a href=\"/community/q/user/ryanod\" class=\"pull-left\">\n\t\t\t\t\t\n\t\t\t\t\t<img class=\"avatar not-responsive avatar-rounded\" alt=\"RyanOD\" title=\"RyanOD\" data-uid=\"5203\" loading=\"lazy\" component=\"avatar/icon\" src=\"https://moz.com/avatar/large/3/r.png\"><\/img>\n\t\t\t\t\t\n\t\t\t\t<\/a>\n\t\t\t\t\n\t\t\t<\/div>\n\n\t\t\t<h3 component=\"topic/header\" class=\"title\">\n\t\t\t\t<i component=\"topic/pinned\" class=\"fa fa-thumb-tack hide\" title=\"Pinned\"><\/i>\n\t\t\t\t<i component=\"topic/locked\" class=\"fa fa-lock \" title=\"Locked\"><\/i>\n\t\t\t\t<i component=\"topic/moved\" class=\"fa fa-arrow-circle-right hide\" title=\"Moved\"><\/i>\n\t\t\t\t\n\n\t\t\t\t\n\t\t\t\t<a href=\"/community/q/topic/38135/varying-internal-link-anchor-text-with-each-new-page-load/7\" itemprop=\"url\">Varying Internal Link Anchor Text with Each New Page Load<\/a><br />\n\t\t\t\t\n\t\t\t<\/h3>\n\n\t\t\t\n\n\t\t\t<div class=\"category-content\">\n\t\t\t\t\n\t\t\t\t<p dir=\"auto\">I'm asking for people's opinions on varying internal anchor text. Before you jump in and say, \"Oh yes, varying your anchor text is always a good idea\", let me explain.\nI'm not talking about varying anchor text on different links scattered throughout a site. We all know that is a wise thing to do for a variety of reasons that have been covered in many places. What I'm talking about is including semi-useful links below the fold and then varying the anchor text with each page load. Each time Googlebot crawls a page, it sees different anchor text for each link. That way, Googlebot is seeing, for example, 'san diego bars', 'taverns in san diego', 'san diego clubs', and 'pubs in san diego' all pointing to a San Diego bar/tavern/club/pub page.\nI'm wondering if there is value in this approach. Will it help a site rank well for multiple search queries? Could it potentially be better than static anchor text as it may help Google better understand the targeted page? Is it a good way to protect a large site with a huge number of internal links from Penguin?\nTo summarize, we're talking about the impact of varying the anchor text on a single page with each page load as opposed to varying the anchor text on different pages.\nThoughts?\n<\/p>\n\t\t\t\t\n\t\t\t\t\n\t\t\t\t<small class=\"category-name\">\n\t\t\t\t\t<a href=\"/community/q/category/16/intermediate-advanced-seo\"><span class=\"fa-stack fa-lg\" style=\"background-color: #fc4949; color: #FFFFFF;\"><i style=\"color:#FFFFFF;\" class=\"fa fa-graduation-cap fa-stack-1x\"><\/i><\/span> Intermediate &amp; Advanced SEO<\/a> |\n\t\t\t\t<\/small>\n\t\t\t\t\n\n\t\t\t\t<small>\n\t\t\t\t\t\n\t\t\t\t\t<span class=\"timeago\" title=\"2013-07-22T04:08:45.000Z\"><\/span>\n\t\t\t\t\t| <a href=\"/community/q/user/ryanod\">RyanOD<\/a>\n\t\t\t\t\t\n\t\t\t\t<\/small>\n\t\t\t<\/div>\n\n\t\t\t\n\t\t\t<div class=\"votes\" title=\"Votes\">\n\t\t\t\t<i class=\"fa fa-thumbs-up\"><\/i> <span class=\"human-readable-number\" title=\"0\">0<\/span>\n\t\t\t<\/div>\n\t\t\t\n\t\t<\/div>\n\t<\/li>\n\t\n\t<li component=\"category/topic\" class=\"clearfix category-item locked unread \" data-tid=\"19725\" data-index=\"6\" data-cid=\"16\" itemprop=\"itemListElement\" itemscope itemtype=\"https://schema.org/ListItem\">\n\t\t<link itemprop=\"url\" content=\"/community/q/topic/19725/landing-page-home-page-redesign-seo-factor-question-serious-concern\" />\n\t\t<meta itemprop=\"name\" content=\"Landing Page - Home Page redesign SEO factor question - Serious concern.\" />\n\t\t<meta itemprop=\"itemListOrder\" content=\"descending\" />\n\t\t<meta itemprop=\"position\" content=\"7\" />\n\t\t<a id=\"6\" data-index=\"6\" component=\"topic/anchor\"><\/a>\n\n\t\t<div class=\"content\">\n\t\t\t<div class=\"avatar pull-left\">\n\t\t\t\t\n\n\t\t\t\t\n\t\t\t\t<a href=\"/community/q/user/meninkilts\" class=\"pull-left\">\n\t\t\t\t\t\n\t\t\t\t\t<img class=\"avatar not-responsive avatar-rounded\" alt=\"MenInKilts\" title=\"MenInKilts\" data-uid=\"36591\" loading=\"lazy\" component=\"avatar/picture\" src=\"/community/q/assets/uploads/profile/36591-profileavatar-1619579317274.png\" style=\"width: 46px; height: 46px; line-height: 46px; font-size: 2.875rem;\" />\n\t\t\t\t\t\n\t\t\t\t<\/a>\n\t\t\t\t\n\t\t\t<\/div>\n\n\t\t\t<h3 component=\"topic/header\" class=\"title\">\n\t\t\t\t<i component=\"topic/pinned\" class=\"fa fa-thumb-tack hide\" title=\"Pinned\"><\/i>\n\t\t\t\t<i component=\"topic/locked\" class=\"fa fa-lock \" title=\"Locked\"><\/i>\n\t\t\t\t<i component=\"topic/moved\" class=\"fa fa-arrow-circle-right hide\" title=\"Moved\"><\/i>\n\t\t\t\t\n\n\t\t\t\t\n\t\t\t\t<a href=\"/community/q/topic/19725/landing-page-home-page-redesign-seo-factor-question-serious-concern/8\" itemprop=\"url\">Landing Page - Home Page redesign SEO factor question - Serious concern.<\/a><br />\n\t\t\t\t\n\t\t\t<\/h3>\n\n\t\t\t\n\n\t\t\t<div class=\"category-content\">\n\t\t\t\t\n\t\t\t\t<p dir=\"auto\">Hi Folks,\nI'm considering making a big change to our website and really need some expert advise. Will we lose ranking if we do what I propose?\nOur site www.meninkilts.com, needs to split users/clients by \"Commercial\" and \"Residential\" so we can message/market completely differently to each client.\nWe are considering doing this structure:\nLanding Page\n|\n|\nCommercial Homepage  Residential Homepage\nRight now we rank well, for our keywords like \"Window Cleaning cityname\" but are worried that adding a landing page, and splitting our site to two homepages will effect seo (ie: a landing page would only have two buttons: one for commercial and one for residential).\nWhat would be the best way to handle this. Looking forward to your insights!\nCheers Brent\n<\/p>\n\t\t\t\t\n\t\t\t\t\n\t\t\t\t<small class=\"category-name\">\n\t\t\t\t\t<a href=\"/community/q/category/16/intermediate-advanced-seo\"><span class=\"fa-stack fa-lg\" style=\"background-color: #fc4949; color: #FFFFFF;\"><i style=\"color:#FFFFFF;\" class=\"fa fa-graduation-cap fa-stack-1x\"><\/i><\/span> Intermediate &amp; Advanced SEO<\/a> |\n\t\t\t\t<\/small>\n\t\t\t\t\n\n\t\t\t\t<small>\n\t\t\t\t\t\n\t\t\t\t\t<span class=\"timeago\" title=\"2012-06-07T13:12:36.000Z\"><\/span>\n\t\t\t\t\t| <a href=\"/community/q/user/meninkilts\">MenInKilts<\/a>\n\t\t\t\t\t\n\t\t\t\t<\/small>\n\t\t\t<\/div>\n\n\t\t\t\n\t\t\t<div class=\"votes\" title=\"Votes\">\n\t\t\t\t<i class=\"fa fa-thumbs-up\"><\/i> <span class=\"human-readable-number\" title=\"0\">0<\/span>\n\t\t\t<\/div>\n\t\t\t\n\t\t<\/div>\n\t<\/li>\n\t\n\t<li component=\"category/topic\" class=\"clearfix category-item locked unread \" data-tid=\"8784\" data-index=\"7\" data-cid=\"16\" itemprop=\"itemListElement\" itemscope itemtype=\"https://schema.org/ListItem\">\n\t\t<link itemprop=\"url\" content=\"/community/q/topic/8784/does-a-page-on-a-site-with-high-domain-authority-build-page-authority-easier-i-e-less-inbound-links\" />\n\t\t<meta itemprop=\"name\" content=\"Does a page on a site with high domain authority build page authority easier? i.e. less inbound links?\" />\n\t\t<meta itemprop=\"itemListOrder\" content=\"descending\" />\n\t\t<meta itemprop=\"position\" content=\"8\" />\n\t\t<a id=\"7\" data-index=\"7\" component=\"topic/anchor\"><\/a>\n\n\t\t<div class=\"content\">\n\t\t\t<div class=\"avatar pull-left\">\n\t\t\t\t\n\n\t\t\t\t\n\t\t\t\t<a href=\"/community/q/user/adriandg\" class=\"pull-left\">\n\t\t\t\t\t\n\t\t\t\t\t<img class=\"avatar not-responsive avatar-rounded\" alt=\"adriandg\" title=\"adriandg\" data-uid=\"20721\" loading=\"lazy\" component=\"avatar/picture\" src=\"https://moz.com/avatar/user/264819\" style=\"width: 46px; height: 46px; line-height: 46px; font-size: 2.875rem;\" />\n\t\t\t\t\t\n\t\t\t\t<\/a>\n\t\t\t\t\n\t\t\t<\/div>\n\n\t\t\t<h3 component=\"topic/header\" class=\"title\">\n\t\t\t\t<i component=\"topic/pinned\" class=\"fa fa-thumb-tack hide\" title=\"Pinned\"><\/i>\n\t\t\t\t<i component=\"topic/locked\" class=\"fa fa-lock \" title=\"Locked\"><\/i>\n\t\t\t\t<i component=\"topic/moved\" class=\"fa fa-arrow-circle-right hide\" title=\"Moved\"><\/i>\n\t\t\t\t\n\n\t\t\t\t\n\t\t\t\t<a href=\"/community/q/topic/8784/does-a-page-on-a-site-with-high-domain-authority-build-page-authority-easier-i-e-less-inbound-links/6\" itemprop=\"url\">Does a page on a site with high domain authority build page authority easier? i.e. less inbound links?<\/a><br />\n\t\t\t\t\n\t\t\t<\/h3>\n\n\t\t\t\n\n\t\t\t<div class=\"category-content\">\n\t\t\t\t\n\t\t\t\t<p dir=\"auto\">Is this also why people build backlinks to their BBB profiles, Yellowpages Profiles, etc. i.e. why do people build backlinks to other pages that link to them?  Wouldn't it be more beneficial to just build that backlink directly to your target?\n<\/p>\n\t\t\t\t\n\t\t\t\t\n\t\t\t\t<small class=\"category-name\">\n\t\t\t\t\t<a href=\"/community/q/category/16/intermediate-advanced-seo\"><span class=\"fa-stack fa-lg\" style=\"background-color: #fc4949; color: #FFFFFF;\"><i style=\"color:#FFFFFF;\" class=\"fa fa-graduation-cap fa-stack-1x\"><\/i><\/span> Intermediate &amp; Advanced SEO<\/a> |\n\t\t\t\t<\/small>\n\t\t\t\t\n\n\t\t\t\t<small>\n\t\t\t\t\t\n\t\t\t\t\t<span class=\"timeago\" title=\"2011-10-04T15:30:53.000Z\"><\/span>\n\t\t\t\t\t| <a href=\"/community/q/user/adriandg\">adriandg<\/a>\n\t\t\t\t\t\n\t\t\t\t<\/small>\n\t\t\t<\/div>\n\n\t\t\t\n\t\t\t<div class=\"votes\" title=\"Votes\">\n\t\t\t\t<i class=\"fa fa-thumbs-up\"><\/i> <span class=\"human-readable-number\" title=\"0\">0<\/span>\n\t\t\t<\/div>\n\t\t\t\n\t\t<\/div>\n\t<\/li>\n\t\n<\/ul>\n\n\t<\/div>\n<\/div>\n"}]}}</script>		</div><!-- /.container#content -->
	</main>

	<div class="moz-theme moz-footer-wrapper">
		<link type="text/css" href="https://moz.com/assets/dist/styles/components/footer-1242048c.min.css" rel="stylesheet">
<link type="text/css" href="https://moz.com/assets/dist/styles/components/snippets-grid-77f24533.min.css" rel="stylesheet">



  
  <footer class="mzr-footer">
    <div class="mzr-container mzr-skinny-footer">
      <div class="mzr-row mzr-justify-space-between">
        <div class="mzr-col-12 mzr-col-lg">
          <div class="mzr-footer-logo">
            <a href="https://moz.com/">
              
<svg aria-labelledby="moz-logo-title-footer" role="img" width="85" height="25">
  <title id="moz-logo-title-footer">Moz logo</title>
  <path d="M71 16L82.99 3h-25.1c-.48.018-.866.4-.89.882v2.736C54.697 2.696 49.97 0 44.5 0 38.036 0 32.61 3.76 31 8.863V3h-4.38c-1.043.015-1.957.478-2.62 1.177l-8.498 9.325L7 4.177C6.34 3.477 5.427 3.015 4.383 3H0v19h5.117c.492-.024.863-.42.883-.91V12l9.5 10.5L25 12v9.09c.017.49.415.886.905.91H31v-6.863C32.61 20.24 38.036 24 44.5 24c7.732 0 14-5.373 14-12 0-1.038-.17-2.04-.46-3H69L57 22h25.104c.48-.018.872-.403.896-.884V16H71zm-26.452 1.96c-3.764 0-6.818-2.668-6.818-5.96 0-3.293 3.053-5.96 6.818-5.96 3.768 0 6.822 2.668 6.822 5.96s-3.053 5.96-6.822 5.96z"></path>
</svg>
            </a>
          </div>
        </div>
                <div class="mzr-col-12 mzr-col-lg-7 mzr-col-xl-8">
          <ul class="mzr-footer-links">
                                                        <li class="mzr-footer-nav-item">
                  <a href="https://moz.com/about/contact">Contact</a>
                </li>
                                                                      <li class="mzr-footer-nav-item">
                  <a href="https://moz.com/community">Community</a>
                </li>
                                                                      <li class="mzr-footer-nav-item">
                  <a href="https://moz.com/moz-pro-free-trial">Free Trial</a>
                </li>
                                                                      <li class="mzr-footer-nav-item">
                  <a href="https://moz.com/privacy-policy">Terms &amp; Privacy</a>
                </li>
                                                                      <li class="mzr-footer-nav-item">
                  <a href="https://www.ziffdavis.com/accessibility">Accessibility</a>
                </li>
                                                                      <li class="mzr-footer-nav-item">
                  <a href="https://moz.com/about/jobs">Jobs</a>
                </li>
                                                                      <li class="mzr-footer-nav-item">
                  <a href="https://moz.com/help">Help</a>
                </li>
                                                                      <li class="mzr-footer-nav-item">
                  <a href="https://moz.com/whats-new">What&#039;s New</a>
                </li>
                                                                      <li class="mzr-footer-nav-item">
                  <a href="https://moz.com/about/news">News &amp; Press</a>
                </li>
                                                                      <li class="mzr-footer-nav-item">
                  <a href="https://moz.com/mozcon">MozCon</a>
                </li>
                                    </ul>
        </div>
        <div class="mzr-col-12 mzr-col-lg mzr-text-center mzr-text-lg-right">
          <div class="mzr-social-links-footer">
                                                            
                        



<ul class="social-buttons social-buttons-horizontal social-buttons-small">
      <li class="social-button social-button-twitter">
      <a target="_blank" rel="noreferrer  noopener" title="link to Twitter" href="https://twitter.com/Moz">
          
  

  <svg class="icon small icon-twitter" >
    <use href="#icon-twitter">
  </svg>

      </a>
    </li>
        <li class="social-button social-button-facebook">
      <a target="_blank" rel="noreferrer  noopener" title="link to Facebook" href="https://www.facebook.com/moz/">
          
  

  <svg class="icon small icon-facebook" >
    <use href="#icon-facebook">
  </svg>

      </a>
    </li>
        <li class="social-button social-button-instagram">
      <a target="_blank" rel="noreferrer  noopener" title="link to Instagram" href="https://www.instagram.com/moz_hq/">
          
  

  <svg class="icon small icon-instagram" >
    <use href="#icon-instagram">
  </svg>

      </a>
    </li>
        <li class="social-button social-button-linkedin">
      <a target="_blank" rel="noreferrer  noopener" title="link to Linkedin" href="https://www.linkedin.com/company/moz/">
          
  

  <svg class="icon small icon-linkedin" >
    <use href="#icon-linkedin">
  </svg>

      </a>
    </li>
        <li class="social-button social-button-youtube">
      <a target="_blank" rel="noreferrer  noopener" title="link to youtube" href="https://www.youtube.com/channel/UCs26XZBwrSZLiTEH8wcoVXw">
          
  

  <svg class="icon small icon-youtube" >
    <use href="#icon-youtube">
  </svg>

      </a>
    </li>
  </ul>
          </div>
        </div>
      </div>
      <div class="mzr-row mzr-justify-content-center mzr-mt-4">
        <div class="mzr-col">
          <div class="mzr-copyright mzr-text-center">
            © 2021 - 2024 SEOMoz, Inc., a Ziff Davis company. All rights reserved. Moz is a registered trademark of SEOMoz, Inc.
          </div>
        </div>
      </div>
    </div>
  </footer>




  <script>(function() {
    var container = document.querySelector('.mzr-footer');
    var mozIcons = document.getElementById('moz-icons');
    if (container === null || mozIcons !== null) {
      return;
    }
    var icon = document.createElement('div');
    icon.id = 'moz-icons';
    icon.style = 'display:none;';
    document.querySelector('.mzr-footer').appendChild(icon);

    var request = new XMLHttpRequest();
    request.open('GET', 'https://moz.com/assets/dist/icons/icons-dc9b7dbe.min.svg', true);
    request.onload = function() {
      if (request.status >= 200 && request.status < 400) {
        var resp = request.responseText;

        document.getElementById('moz-icons').innerHTML = resp;
      }
    };
    request.send();
  })();</script>
<script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'8d2c16d68ae1fabe',t:'MTcyODk1NjMwMi4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script>
	</div>

	
	<div class="topic-search hidden">
		<div class="btn-group">
			<button type="button" class="btn btn-default count"></button>
			<button type="button" class="btn btn-default prev"><i class="fa fa-fw fa-angle-up"></i></button>
			<button type="button" class="btn btn-default next"><i class="fa fa-fw fa-angle-down"></i></button>
		</div>
	</div>

	<div component="toaster/tray" class="alert-window">
		<div id="reconnect-alert" class="alert alert-dismissable alert-warning clearfix hide" component="toaster/toast">
			<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button>
			<p>Looks like your connection to Moz was lost, please wait while we try to reconnect.</p>
		</div>
	</div>
	

	<div class="hide">
	
	</div>

	<script defer src="/community/q/assets/nodebb.min.js?v=4jds23d1a2r"></script>



<script>
    document.documentElement.style.setProperty('--panel-offset', `${localStorage.getItem('panelOffset') || 0}px`);

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', prepareFooter);
    } else {
        prepareFooter();
    }

    function prepareFooter() {
        
        
        

        $(document).ready(function () {
            app.coldLoad();
        });
    }
</script>
<script>(function(){function c(){var b=a.contentDocument||a.contentWindow.document;if(b){var d=b.createElement('script');d.innerHTML="window.__CF$cv$params={r:'8d2c1f99b83f866f',t:'MTcyODk1NjY2MS4wMDAwMDA='};var a=document.createElement('script');a.nonce='';a.src='/cdn-cgi/challenge-platform/scripts/jsd/main.js';document.getElementsByTagName('head')[0].appendChild(a);";b.getElementsByTagName('head')[0].appendChild(d)}}if(document.body){var a=document.createElement('iframe');a.height=1;a.width=1;a.style.position='absolute';a.style.top=0;a.style.left=0;a.style.border='none';a.style.visibility='hidden';document.body.appendChild(a);if('loading'!==document.readyState)c();else if(window.addEventListener)document.addEventListener('DOMContentLoaded',c);else{var e=document.onreadystatechange||function(){};document.onreadystatechange=function(b){e(b);'loading'!==document.readyState&&(document.onreadystatechange=e,c())}}}})();</script></body>
</html>'''
                links = crawler.extract_links(test_string)
                print(links)

            basic_strings()
            complex_strings()
            negatives()
            webpage_string()

        test_link()
    test_regex()
                
def main():
    # test_fetch()
    test_webcrawler()

main()