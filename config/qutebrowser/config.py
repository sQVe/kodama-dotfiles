# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Aliases for commands. The keys of the given dictionary are the
# aliases, while the values are the commands they map to.
# Type: Dict
c.aliases = {
    'q': 'close',
    'qa': 'quit',
    'w': 'session-save',
    'wqa': 'quit --save'
}

# Require a confirmation before quitting the application.
# Type: ConfirmQuit
# Valid values:
#   - always: Always show a confirmation.
#   - multiple-tabs: Show a confirmation if multiple tabs are opened.
#   - downloads: Show a confirmation if downloads are running
#   - never: Never show a confirmation.
c.confirm_quit = ['never']

# Maximum time (in minutes) between two history items for them to be
# considered being from the same browsing session. Items with less time
# between them are grouped when being displayed in `:history`. Use -1 to
# disable separation.
# Type: Int
c.history_gap_interval = 30

# When to find text on a page case-insensitively.
# Type: String
# Valid values:
#   - always: Search case-insensitively.
#   - never: Search case-sensitively.
#   - smart: Search case-sensitively if there are capital characters.
c.search.ignore_case = 'smart'

# Find text on a page incrementally, renewing the search for each typed
# character.
# Type: Bool
c.search.incremental = True

# How to open links in an existing instance if a new one is launched.
# This happens when e.g. opening a link from a terminal. See
# `new_instance_open_target_window` to customize in which window the
# link is opened in.
# Type: String
# Valid values:
#   - tab: Open a new tab in the existing window and activate the window.
#   - tab-bg: Open a new background tab in the existing window and activate the window.
#   - tab-silent: Open a new tab in the existing window without activating the window.
#   - tab-bg-silent: Open a new background tab in the existing window without activating the window.
#   - window: Open in a new window.
c.new_instance_open_target = 'tab'

# Which window to choose when opening links as new tabs. When
# `new_instance_open_target` is not set to `window`, this is ignored.
# Type: String
# Valid values:
#   - first-opened: Open new tabs in the first (oldest) opened window.
#   - last-opened: Open new tabs in the last (newest) opened window.
#   - last-focused: Open new tabs in the most recently focused window.
#   - last-visible: Open new tabs in the most recently visible window.
c.new_instance_open_target_window = 'last-focused'

# Name of the session to save by default. If this is set to null, the
# session which was last loaded is saved.
# Type: SessionName
c.session.default_name = None

# Load a restored tab as soon as it takes focus.
# Type: Bool
c.session.lazy_restore = False

# Backend to use to display websites. qutebrowser supports two different
# web rendering engines / backends, QtWebKit and QtWebEngine. QtWebKit
# was discontinued by the Qt project with Qt 5.6, but picked up as a
# well maintained fork: https://github.com/annulen/webkit/wiki -
# qutebrowser only supports the fork. QtWebEngine is Qt's official
# successor to QtWebKit. It's slightly more resource hungry than
# QtWebKit and has a couple of missing features in qutebrowser, but is
# generally the preferred choice.
# Type: String
# Valid values:
#   - webengine: Use QtWebEngine (based on Chromium).
#   - webkit: Use QtWebKit (based on WebKit, similar to Safari).
c.backend = 'webengine'

# Additional arguments to pass to Qt, without leading `--`. With
# QtWebEngine, some Chromium arguments (see
# https://peter.sh/experiments/chromium-command-line-switches/ for a
# list) will work.
# Type: List of String
c.qt.args = ['ppapi-widevine-path=/usr/lib/qt/plugins/ppapi/libwidevinecdmadapter.so']

# Force a Qt platform to use. This sets the `QT_QPA_PLATFORM`
# environment variable and is useful to force using the XCB plugin when
# running QtWebEngine on Wayland.
# Type: String
c.qt.force_platform = None

# Turn on Qt HighDPI scaling. This is equivalent to setting
# QT_AUTO_SCREEN_SCALE_FACTOR=1 in the environment. It's off by default
# as it can cause issues with some bitmap fonts. As an alternative to
# this, it's possible to set font sizes and the `zoom.default` setting.
# Type: Bool
c.qt.highdpi = False

# Time interval (in milliseconds) between auto-saves of
# config/cookies/etc.
# Type: Int
c.auto_save.interval = 15000

# Always restore open sites when qutebrowser is reopened.
# Type: Bool
c.auto_save.session = False

# Size (in bytes) of the HTTP network cache. Null to use the default
# value. With QtWebEngine, the maximum supported value is 2147483647 (~2
# GB).
# Type: Int
c.content.cache.size = None

# Store cookies. Note this option needs a restart with QtWebEngine on Qt
# < 5.9.
# Type: Bool
c.content.cookies.store = True

# Default encoding to use for websites. The encoding must be a string
# describing an encoding such as _utf-8_, _iso-8859-1_, etc.
# Type: String
c.content.default_encoding = 'iso-8859-1'

# Limit fullscreen to the browser window (does not expand to fill the
# screen).
# Type: Bool
c.content.windowed_fullscreen = False

# Allow websites to request geolocations.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
c.content.geolocation = 'ask'

# Value to send in the `Accept-Language` header. Note that the value
# read from JavaScript is always the global value.
# Type: String
c.content.headers.accept_language = 'en-US,en'

# Custom headers for qutebrowser HTTP requests.
# Type: Dict
c.content.headers.custom = {}

# Value to send in the `DNT` header. When this is set to true,
# qutebrowser asks websites to not track your identity. If set to null,
# the DNT header is not sent at all.
# Type: Bool
c.content.headers.do_not_track = True

# User agent to send. Unset to send the default. Note that the value
# read from JavaScript is always the global value.
# Type: String
c.content.headers.user_agent = None

# Enable host blocking.
# Type: Bool
c.content.host_blocking.enabled = True

# List of URLs of lists which contain hosts to block.  The file can be
# in one of the following formats:  - An `/etc/hosts`-like file - One
# host per line - A zip-file of any of the above, with either only one
# file, or a file   named `hosts` (with any extension).  It's also
# possible to add a local file or directory via a `file://` URL. In case
# of a directory, all files in the directory are read as adblock lists.
# The file `~/.config/qutebrowser/blocked-hosts` is always read if it
# exists.
# Type: List of Url
c.content.host_blocking.lists = ['https://www.malwaredomainlist.com/hostslist/hosts.txt', 'http://someonewhocares.org/hosts/hosts', 'http://winhelp2002.mvps.org/hosts.zip', 'http://malwaredomains.lehigh.edu/files/justdomains.zip', 'https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&mimetype=plaintext']

# A list of patterns that should always be loaded, despite being ad-
# blocked. Local domains are always exempt from hostblocking.
# Type: List of UrlPattern
c.content.host_blocking.whitelist = ['piwik.org']

# Enable hyperlink auditing (`<a ping>`).
# Type: Bool
c.content.hyperlink_auditing = False

# Load images automatically in web pages.
# Type: Bool
c.content.images = True

# Show javascript alerts.
# Type: Bool
c.content.javascript.alert = True

# Allow JavaScript to read from or write to the clipboard. With
# QtWebEngine, writing the clipboard as response to a user interaction
# is always allowed.
# Type: Bool
c.content.javascript.can_access_clipboard = False

# Allow JavaScript to open new tabs without user interaction.
# Type: Bool
c.content.javascript.can_open_tabs_automatically = False

# Enable JavaScript.
# Type: Bool
c.content.javascript.enabled = True

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'file://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

# Log levels to use for JavaScript console logging messages. When a
# JavaScript message with the level given in the dictionary key is
# logged, the corresponding dictionary value selects the qutebrowser
# logger to use. On QtWebKit, the "unknown" setting is always used.
# Type: Dict
c.content.javascript.log = {'unknown': 'debug', 'info': 'debug', 'warning': 'debug', 'error': 'debug'}

# Use the standard JavaScript modal dialog for `alert()` and
# `confirm()`.
# Type: Bool
c.content.javascript.modal_dialog = False

# Show javascript prompts.
# Type: Bool
c.content.javascript.prompt = True

# Allow locally loaded documents to access remote URLs.
# Type: Bool
c.content.local_content_can_access_remote_urls = False

# Allow locally loaded documents to access other local URLs.
# Type: Bool
c.content.local_content_can_access_file_urls = True

# Enable support for HTML 5 local storage and Web SQL.
# Type: Bool
c.content.local_storage = True

# Allow websites to record audio/video.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
c.content.media_capture = 'ask'

# Netrc-file for HTTP authentication. If unset, `~/.netrc` is used.
# Type: File
c.content.netrc_file = None

# Enable plugins in Web pages.
# Type: Bool
c.content.plugins = False

# Draw the background color and images also when the page is printed.
# Type: Bool
c.content.print_element_backgrounds = True

# Open new windows in private browsing mode which does not record
# visited pages.
# Type: Bool
c.content.private_browsing = False

# Proxy to use. In addition to the listed values, you can use a
# `socks://...` or `http://...` URL.
# Type: Proxy
# Valid values:
#   - system: Use the system wide proxy.
#   - none: Don't use any proxy
c.content.proxy = 'system'

# Validate SSL handshakes.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
c.content.ssl_strict = 'ask'

# List of user stylesheet filenames to use.
# Type: List of File, or File
c.content.user_stylesheets = []

# Enable WebGL.
# Type: Bool
c.content.webgl = True

# Monitor load requests for cross-site scripting attempts. Suspicious
# scripts will be blocked and reported in the inspector's JavaScript
# console.
# Type: Bool
c.content.xss_auditing = False

# Number of commands to save in the command history. 0: no history / -1:
# unlimited
# Type: Int
c.completion.cmd_history_max_items = -1

# Height (in pixels or as percentage of the window) of the completion.
# Type: PercOrInt
c.completion.height = '50%'

# Move on to the next part when there's only one possible completion
# left.
# Type: Bool
c.completion.quick = True

# When to show the autocompletion window.
# Type: String
# Valid values:
#   - always: Whenever a completion is available.
#   - auto: Whenever a completion is requested.
#   - never: Never.
c.completion.show = 'always'

# Shrink the completion to be smaller than the configured size if there
# are no scrollbars.
# Type: Bool
c.completion.shrink = False

# Width (in pixels) of the scrollbar in the completion window.
# Type: Int
c.completion.scrollbar.width = 12

# Padding (in pixels) of the scrollbar handle in the completion window.
# Type: Int
c.completion.scrollbar.padding = 2

# Format of timestamps (e.g. for the history completion).
# Type: TimestampTemplate
c.completion.timestamp_format = '%Y-%m-%d'

# Number of URLs to show in the web history. 0: no history / -1:
# unlimited
# Type: Int
c.completion.web_history.max_items = -1

# Delay (in milliseconds) before updating completions after typing a
# character.
# Type: Int
c.completion.delay = 0

# Minimum amount of characters needed to update completions.
# Type: Int
c.completion.min_chars = 1

# Execute the best-matching command on a partial match.
# Type: Bool
c.completion.use_best_match = False

# Directory to save downloads to. If unset, a sensible OS-specific
# default is used.
# Type: Directory
c.downloads.location.directory = None

# Prompt the user for the download location. If set to false,
# `downloads.location.directory` will be used.
# Type: Bool
c.downloads.location.prompt = True

# Remember the last used download directory.
# Type: Bool
c.downloads.location.remember = True

# What to display in the download filename input.
# Type: String
# Valid values:
#   - path: Show only the download path.
#   - filename: Show only download filename.
#   - both: Show download path and filename.
c.downloads.location.suggestion = 'path'

# Default program used to open downloads. If null, the default internal
# handler is used. Any `{}` in the string will be expanded to the
# filename, else the filename will be appended.
# Type: String
c.downloads.open_dispatcher = None

# Where to show the downloaded files.
# Type: VerticalPosition
# Valid values:
#   - top
#   - bottom
c.downloads.position = 'top'

# Duration (in milliseconds) to wait before removing finished downloads.
# If set to -1, downloads are never removed.
# Type: Int
c.downloads.remove_finished = -1

# Editor (and arguments) to use for the `open-editor` command. The
# following placeholders are defined: * `{file}`: Filename of the file
# to be edited. * `{line}`: Line in which the caret is found in the
# text. * `{column}`: Column in which the caret is found in the text. *
# `{line0}`: Same as `{line}`, but starting from index 0. * `{column0}`:
# Same as `{column}`, but starting from index 0.
# Type: ShellCommand
c.editor.command = ['urxvt', '-name', 'vim-qutebrowser', '-e', 'nvim', '{file}']

# Encoding to use for the editor.
# Type: Encoding
c.editor.encoding = 'utf-8'

# When a hint can be automatically followed without pressing Enter.
# Type: String
# Valid values:
#   - always: Auto-follow whenever there is only a single hint on a page.
#   - unique-match: Auto-follow whenever there is a unique non-empty match in either the hint string (word mode) or filter (number mode).
#   - full-match: Follow the hint when the user typed the whole hint (letter, word or number mode) or the element's text (only in number mode).
#   - never: The user will always need to press Enter to follow a hint.
c.hints.auto_follow = 'unique-match'

# Duration (in milliseconds) to ignore normal-mode key bindings after a
# successful auto-follow.
# Type: Int
c.hints.auto_follow_timeout = 0

# CSS border value for hints.
# Type: String
c.hints.border = '1px solid #000'

# Characters used for hint strings.
# Type: UniqueCharString
c.hints.chars = 'asdfghjklqweruiopzxcvnm'

# Dictionary file to be used by the word hints.
# Type: File
c.hints.dictionary = '/usr/share/dict/words'

# Hide unmatched hints in rapid mode.
# Type: Bool
c.hints.hide_unmatched_rapid_hints = True

# Minimum number of characters used for hint strings.
# Type: Int
c.hints.min_chars = 1

# Mode to use for hints.
# Type: String
# Valid values:
#   - number: Use numeric hints. (In this mode you can also type letters from the hinted element to filter and reduce the number of elements that are hinted.)
#   - letter: Use the characters in the `hints.chars` setting.
#   - word: Use hints words based on the html elements and the extra words.
c.hints.mode = 'letter'

# Comma-separated list of regular expressions to use for 'next' links.
# Type: List of Regex
c.hints.next_regexes = ['\\bnext\\b', '\\bmore\\b', '\\bnewer\\b', '\\b[>→≫]\\b', '\\b(>>|»)\\b', '\\bcontinue\\b']

# Comma-separated list of regular expressions to use for 'prev' links.
# Type: List of Regex
c.hints.prev_regexes = ['\\bprev(ious)?\\b', '\\bback\\b', '\\bolder\\b', '\\b[<←≪]\\b', '\\b(<<|«)\\b']

# Scatter hint key chains (like Vimium) or not (like dwb). Ignored for
# number hints.
# Type: Bool
c.hints.scatter = True

# Make characters in hint strings uppercase.
# Type: Bool
c.hints.uppercase = True

# Which unbound keys to forward to the webview in normal mode.
# Type: String
# Valid values:
#   - all: Forward all unbound keys.
#   - auto: Forward unbound non-alphanumeric keys.
#   - none: Don't forward any keys.
c.input.forward_unbound_keys = 'auto'

# Automatically enter insert mode if an editable element is focused
# after loading the page.
# Type: Bool
c.input.insert_mode.auto_load = False

# Leave insert mode if a non-editable element is clicked.
# Type: Bool
c.input.insert_mode.auto_leave = True

# Switch to insert mode when clicking flash and other plugins.
# Type: Bool
c.input.insert_mode.plugins = False

# Include hyperlinks in the keyboard focus chain when tabbing.
# Type: Bool
c.input.links_included_in_focus_chain = True

# Timeout (in milliseconds) for partially typed key bindings. If the
# current input forms only partial matches, the keystring will be
# cleared after this time.
# Type: Int
c.input.partial_timeout = 5000

# Enable Opera-like mouse rocker gestures. This disables the context
# menu.
# Type: Bool
c.input.rocker_gestures = False

# Enable spatial navigation. Spatial navigation consists in the ability
# to navigate between focusable elements in a Web page, such as
# hyperlinks and form controls, by using Left, Right, Up and Down arrow
# keys. For example, if the user presses the Right key, heuristics
# determine whether there is an element he might be trying to reach
# towards the right and which element he probably wants.
# Type: Bool
c.input.spatial_navigation = False

# Keychains that shouldn't be shown in the keyhint dialog. Globs are
# supported, so `;*` will blacklist all keychains starting with `;`. Use
# `*` to disable keyhints.
# Type: List of String
c.keyhint.blacklist = []

# Rounding radius (in pixels) for the edges of the keyhint dialog.
# Type: Int
c.keyhint.radius = 6

# Time (in milliseconds) from pressing a key to seeing the keyhint
# dialog.
# Type: Int
c.keyhint.delay = 500

# Duration (in milliseconds) to show messages in the statusbar for. Set
# to 0 to never clear messages.
# Type: Int
c.messages.timeout = 2000

# Show a filebrowser in upload/download prompts.
# Type: Bool
c.prompt.filebrowser = True

# Rounding radius (in pixels) for the edges of prompts.
# Type: Int
c.prompt.radius = 8

# Enable smooth scrolling for web pages. Note smooth scrolling does not
# work with the `:scroll-px` command.
# Type: Bool
c.scrolling.smooth = False

# Languages to use for spell checking. You can check for available
# languages and install dictionaries using scripts/dictcli.py. Run the
# script with -h/--help for instructions.
# Type: List of String
# Valid values:
#   - af-ZA: Afrikaans (South Africa)
#   - bg-BG: Bulgarian (Bulgaria)
#   - ca-ES: Catalan (Spain)
#   - cs-CZ: Czech (Czech Republic)
#   - da-DK: Danish (Denmark)
#   - de-DE: German (Germany)
#   - el-GR: Greek (Greece)
#   - en-AU: English (Australia)
#   - en-CA: English (Canada)
#   - en-GB: English (United Kingdom)
#   - en-US: English (United States)
#   - es-ES: Spanish (Spain)
#   - et-EE: Estonian (Estonia)
#   - fa-IR: Farsi (Iran)
#   - fo-FO: Faroese (Faroe Islands)
#   - fr-FR: French (France)
#   - he-IL: Hebrew (Israel)
#   - hi-IN: Hindi (India)
#   - hr-HR: Croatian (Croatia)
#   - hu-HU: Hungarian (Hungary)
#   - id-ID: Indonesian (Indonesia)
#   - it-IT: Italian (Italy)
#   - ko: Korean
#   - lt-LT: Lithuanian (Lithuania)
#   - lv-LV: Latvian (Latvia)
#   - nb-NO: Norwegian (Norway)
#   - nl-NL: Dutch (Netherlands)
#   - pl-PL: Polish (Poland)
#   - pt-BR: Portuguese (Brazil)
#   - pt-PT: Portuguese (Portugal)
#   - ro-RO: Romanian (Romania)
#   - ru-RU: Russian (Russia)
#   - sh: Serbo-Croatian
#   - sk-SK: Slovak (Slovakia)
#   - sl-SI: Slovenian (Slovenia)
#   - sq: Albanian
#   - sr: Serbian
#   - sv-SE: Swedish (Sweden)
#   - ta-IN: Tamil (India)
#   - tg-TG: Tajik (Tajikistan)
#   - tr-TR: Turkish (Turkey)
#   - uk-UA: Ukrainian (Ukraine)
#   - vi-VN: Vietnamese (Viet Nam)
c.spellcheck.languages = ['en-US', 'sv-SE']

# Hide the statusbar unless a message is shown.
# Type: Bool
c.statusbar.hide = False

# Padding (in pixels) for the statusbar.
# Type: Padding
c.statusbar.padding = {'top': 1, 'bottom': 1, 'left': 0, 'right': 0}

# Position of the status bar.
# Type: VerticalPosition
# Valid values:
#   - top
#   - bottom
c.statusbar.position = 'bottom'

# Open new tabs (middleclick/ctrl+click) in the background.
# Type: Bool
c.tabs.background = True

# Mouse button with which to close tabs.
# Type: String
# Valid values:
#   - right: Close tabs on right-click.
#   - middle: Close tabs on middle-click.
#   - none: Don't close tabs using the mouse.
c.tabs.close_mouse_button = 'middle'

# How to behave when the close mouse button is pressed on the tab bar.
# Type: String
# Valid values:
#   - new-tab: Open a new tab.
#   - close-current: Close the current tab.
#   - close-last: Close the last tab.
#   - ignore: Don't do anything.
c.tabs.close_mouse_button_on_bar = 'new-tab'

# Scaling factor for favicons in the tab bar. The tab size is unchanged,
# so big favicons also require extra `tabs.padding`.
# Type: Float
c.tabs.favicons.scale = 1.0

# How to behave when the last tab is closed.
# Type: String
# Valid values:
#   - ignore: Don't do anything.
#   - blank: Load a blank page.
#   - startpage: Load the start page.
#   - default-page: Load the default page.
#   - close: Close the window.
c.tabs.last_close = 'ignore'

# Switch between tabs using the mouse wheel.
# Type: Bool
c.tabs.mousewheel_switching = True

# Position of new tabs opened from another tab.
# Type: NewTabPosition
# Valid values:
#   - prev: Before the current tab.
#   - next: After the current tab.
#   - first: At the beginning.
#   - last: At the end.
c.tabs.new_position.related = 'next'

# Position of new tabs which aren't opened from another tab.
# Type: NewTabPosition
# Valid values:
#   - prev: Before the current tab.
#   - next: After the current tab.
#   - first: At the beginning.
#   - last: At the end.
c.tabs.new_position.unrelated = 'last'

# Padding (in pixels) around text for tabs.
# Type: Padding
c.tabs.padding = {'top': 2, 'bottom': 2, 'left': 5, 'right': 5}

# Position of the tab bar.
# Type: Position
# Valid values:
#   - top
#   - bottom
#   - left
#   - right
c.tabs.position = 'top'

# Which tab to select when the focused tab is removed.
# Type: SelectOnRemove
# Valid values:
#   - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
#   - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
#   - last-used: Select the previously selected tab.
c.tabs.select_on_remove = 'next'

# When to show the tab bar.
# Type: String
# Valid values:
#   - always: Always show the tab bar.
#   - never: Always hide the tab bar.
#   - multiple: Hide the tab bar if only one tab is open.
#   - switching: Show the tab bar when switching tabs.
c.tabs.show = 'always'

# Duration (in milliseconds) to show the tab bar before hiding it when
# tabs.show is set to 'switching'.
# Type: Int
c.tabs.show_switching_delay = 800

# Open a new window for every tab.
# Type: Bool
c.tabs.tabs_are_windows = False

# Alignment of the text inside of tabs.
# Type: TextAlignment
# Valid values:
#   - left
#   - right
#   - center
c.tabs.title.alignment = 'left'

# Format to use for the tab title. The following placeholders are
# defined:  * `{perc}`: Percentage as a string like `[10%]`. *
# `{perc_raw}`: Raw percentage, e.g. `10`. * `{title}`: Title of the
# current web page. * `{title_sep}`: The string ` - ` if a title is set,
# empty otherwise. * `{index}`: Index of this tab. * `{id}`: Internal
# tab ID of this tab. * `{scroll_pos}`: Page scroll position. *
# `{host}`: Host of the current web page. * `{backend}`: Either
# ''webkit'' or ''webengine'' * `{private}`: Indicates when private mode
# is enabled. * `{current_url}`: URL of the current web page. *
# `{protocol}`: Protocol (http/https/...) of the current web page. *
# `{audio}`: Indicator for audio/mute status.
# Type: FormatString
c.tabs.title.format = '{index}: {title}'

# Format to use for the tab title for pinned tabs. The same placeholders
# like for `tabs.title.format` are defined.
# Type: FormatString
c.tabs.title.format_pinned = '{index}'

# Width (in pixels or as percentage of the window) of the tab bar if
# it's vertical.
# Type: PercOrInt
c.tabs.width = '20%'

# Width (in pixels) of the progress indicator (0 to disable).
# Type: Int
c.tabs.indicator.width = 6

# Padding (in pixels) for tab indicators.
# Type: Padding
c.tabs.indicator.padding = {'bottom': 4, 'left': 0, 'right': 4, 'top': 4}

# Shrink pinned tabs down to their contents.
# Type: Bool
c.tabs.pinned.shrink = True

# Wrap when changing tabs.
# Type: Bool
c.tabs.wrap = True

# What search to start when something else than a URL is entered.
# Type: String
# Valid values:
#   - naive: Use simple/naive check.
#   - dns: Use DNS requests (might be slow!).
#   - never: Never search automatically.
c.url.auto_search = 'naive'

# Page to open if :open -t/-b/-w is used without URL. Use `about:blank`
# for a blank page.
# Type: FuzzyUrl
c.url.default_page = '~/.dotfiles/config/qutebrowser/index.html'

# URL segments where `:navigate increment/decrement` will search for a
# number.
# Type: FlagList
# Valid values:
#   - host
#   - port
#   - path
#   - query
#   - anchor
c.url.incdec_segments = ['path', 'query']

# Open base URL of the searchengine if a searchengine shortcut is
# invoked without parameters.
# Type: Bool
c.url.open_base_url = True

# Search engines which can be used via the address bar. Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` signs. The search engine named
# `DEFAULT` is used when `url.auto_search` is turned on and something
# else than a URL was entered to be opened. Other search engines can be
# used by prepending the search engine name to the search term, e.g.
# `:open google qutebrowser`.
# Type: Dict
c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}'}

# Page(s) to open at the start.
# Type: List of FuzzyUrl, or FuzzyUrl
c.url.start_pages = 'https://devdocs.io'

# URL parameters to strip with `:yank url`.
# Type: List of String
c.url.yank_ignored_parameters = ['ref', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content']

# Format to use for the window title. The same placeholders like for
# `tabs.title.format` are defined.
# Type: FormatString
c.window.title_format = '{perc}{title}{title_sep}qutebrowser'

# Default zoom level.
# Type: Perc
c.zoom.default = '100%'

# Available zoom levels.
# Type: List of Perc
c.zoom.levels = ['25%', '50%', '75%', '100%', '125%', '150%', '175%', '200%', '250%', '300%']

# Number of zoom increments to divide the mouse wheel movements to.
# Type: Int
c.zoom.mouse_divider = 512

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
# Type: List of QtColor, or QtColor
c.colors.completion.fg = ['white', 'white', 'white']

# Background color of the completion widget for odd rows.
# Type: QssColor
c.colors.completion.odd.bg = '#343434'

# Background color of the completion widget for even rows.
# Type: QssColor
c.colors.completion.even.bg = '#383838'

# Foreground color of completion widget category headers.
# Type: QtColor
c.colors.completion.category.fg = '#343434'

# Background color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.bg = '#bd93f9'

# Top border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.top = '#bd93f9'

# Bottom border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.bottom = '#bd93f9'

# Foreground color of the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.fg = '#343434'

# Background color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.bg = '#50fa7b'

# Top border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.item.selected.border.top = '#50fa7b'

# Bottom border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.bottom = '#50fa7b'

# Foreground color of the matched text in the completion.
# Type: QssColor
c.colors.completion.match.fg = '#ff5555'

# Color of the scrollbar handle in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.fg = '#F8F8f2'

# Color of the scrollbar in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.bg = '#343434'

# Background color for the download bar.
# Type: QssColor
c.colors.downloads.bar.bg = '#343434'

# Color gradient start for download text.
# Type: QtColor
c.colors.downloads.start.fg = '#6272a4'

# Color gradient start for download backgrounds.
# Type: QtColor
c.colors.downloads.start.bg = '#f1fa8c'

# Color gradient end for download text.
# Type: QtColor
c.colors.downloads.stop.fg = '#f8f8f2'

# Color gradient stop for download backgrounds.
# Type: QtColor
c.colors.downloads.stop.bg = '#bd93f9'

# Color gradient interpolation system for download text.
# Type: ColorSystem
# Valid values:
#   - rgb: Interpolate in the RGB color system.
#   - hsv: Interpolate in the HSV color system.
#   - hsl: Interpolate in the HSL color system.
#   - none: Don't show a gradient.
c.colors.downloads.system.fg = 'rgb'

# Foreground color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.fg = '#f8f8f2'

# Background color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.bg = '#ff5555'

# Font color for hints.
# Type: QssColor
c.colors.hints.fg = 'black'

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
# Type: QssColor
c.colors.hints.bg = '#ffb86c'

# Font color for the matched part of hints.
# Type: QssColor
c.colors.hints.match.fg = '#bd93f9'

# Text color for the keyhint widget.
# Type: QssColor
c.colors.keyhint.fg = 'white'

# Highlight color for keys to complete the current keychain.
# Type: QssColor
c.colors.keyhint.suffix.fg = '#ffff00'

# Background color of the keyhint widget.
# Type: QssColor
c.colors.keyhint.bg = 'rgba(0, 0, 0, 80%)'

# Foreground color of an error message.
# Type: QssColor
c.colors.messages.error.fg = '#f8f8f2'

# Background color of an error message.
# Type: QssColor
c.colors.messages.error.bg = '#ff5555'

# Border color of an error message.
# Type: QssColor
c.colors.messages.error.border = '#343434'

# Foreground color of a warning message.
# Type: QssColor
c.colors.messages.warning.fg = '#f8f8f2'

# Background color of a warning message.
# Type: QssColor
c.colors.messages.warning.bg = 'darkorange'

# Border color of a warning message.
# Type: QssColor
c.colors.messages.warning.border = '#d47300'

# Foreground color of an info message.
# Type: QssColor
c.colors.messages.info.fg = '#f8f8f2'

# Background color of an info message.
# Type: QssColor
c.colors.messages.info.bg = '#343434'

# Border color of an info message.
# Type: QssColor
c.colors.messages.info.border = '#343434'

# Foreground color for prompts.
# Type: QssColor
c.colors.prompts.fg = '#f8f8f2'

# Border used around UI elements in prompts.
# Type: String
c.colors.prompts.border = '1px solid #ccc'

# Background color for prompts.
# Type: QssColor
c.colors.prompts.bg = '#343434'

# Background color for the selected item in filename prompts.
# Type: QssColor
c.colors.prompts.selected.bg = '#ccc'

# Foreground color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.fg = '#f8f8f2'

# Background color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.bg = '#343434'

# Foreground color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.fg = '#343434'

# Background color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.bg = '#50fa7b'

# Foreground color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.fg = '#343434'

# Background color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.bg = '#bd93f9'

# Foreground color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.fg = '#f8f8f2'

# Background color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.bg = '#666666'

# Foreground color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.fg = '#f8f8f2'

# Background color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.bg = '#343434'

# Foreground color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.fg = '#f8f8f2'

# Background color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.bg = '#666666'

# Foreground color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.fg = '#f8f8f2'

# Background color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.bg = '#bd93f9'

# Foreground color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.fg = '#f8f8f2'

# Background color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.bg = '#a12dff'

# Background color of the progress bar.
# Type: QssColor
c.colors.statusbar.progress.bg = '#ff79c6'

# Default foreground color of the URL in the statusbar.
# Type: QssColor
c.colors.statusbar.url.fg = '#aaaaaa'

# Foreground color of the URL in the statusbar on error.
# Type: QssColor
c.colors.statusbar.url.error.fg = '#ffb86c'

# Foreground color of the URL in the statusbar for hovered links.
# Type: QssColor
c.colors.statusbar.url.hover.fg = '#8be9fd'

# Foreground color of the URL in the statusbar on successful load
# (http).
# Type: QssColor
c.colors.statusbar.url.success.http.fg = '#aaaaaa'

# Foreground color of the URL in the statusbar on successful load
# (https).
# Type: QssColor
c.colors.statusbar.url.success.https.fg = '#aaaaaa'

# Foreground color of the URL in the statusbar when there's a warning.
# Type: QssColor
c.colors.statusbar.url.warn.fg = '#55ffff'

# Background color of the tab bar.
# Type: QtColor
c.colors.tabs.bar.bg = '#343434'

# Color gradient start for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.start = '#f1fa8c'

# Color gradient end for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.stop = '#bd93f9'

# Color for the tab indicator on errors.
# Type: QtColor
c.colors.tabs.indicator.error = '#ff5555'

# Color gradient interpolation system for the tab indicator.
# Type: ColorSystem
# Valid values:
#   - rgb: Interpolate in the RGB color system.
#   - hsv: Interpolate in the HSV color system.
#   - hsl: Interpolate in the HSL color system.
#   - none: Don't show a gradient.
c.colors.tabs.indicator.system = 'rgb'

# Foreground color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.fg = '#aaaaaa'

# Background color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.bg = '#343434'

# Foreground color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.fg = '#aaaaaa'

# Background color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.bg = '#343434'

# Foreground color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.fg = '#50fa7b'

# Background color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.bg = '#444444'

# Foreground color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.fg = '#50fa7b'

# Background color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.bg = '#444444'

# Background color for webpages if unset (or empty to use the theme's
# color).
# Type: QtColor
c.colors.webpage.bg = 'white'

# Default monospace fonts. Whenever "monospace" is used in a font
# setting, it's replaced with the fonts listed here.
# Type: Font
c.fonts.monospace = 'Iosevka, monospace'

# Font used in the completion widget.
# Type: Font
c.fonts.completion.entry = '12px monospace'

# Font used in the completion categories.
# Type: Font
c.fonts.completion.category = 'bold 12px monospace'

# Font used for the debugging console.
# Type: QtFont
c.fonts.debug_console = '12px monospace'

# Font used for the downloadbar.
# Type: Font
c.fonts.downloads = '12px monospace'

# Font used for the hints.
# Type: Font
c.fonts.hints = 'bold 12px monospace'

# Font used in the keyhint widget.
# Type: Font
c.fonts.keyhint = '12px monospace'

# Font used for error messages.
# Type: Font
c.fonts.messages.error = '12px monospace'

# Font used for info messages.
# Type: Font
c.fonts.messages.info = '12px monospace'

# Font used for warning messages.
# Type: Font
c.fonts.messages.warning = '12px monospace'

# Font used for prompts.
# Type: Font
c.fonts.prompts = '12px sans-serif'

# Font used in the statusbar.
# Type: Font
c.fonts.statusbar = '12px monospace'

# Font used in the tab bar.
# Type: QtFont
c.fonts.tabs = '12px monospace'

# Font family for standard fonts.
# Type: FontFamily
c.fonts.web.family.standard = 'Arimo'

# Font family for fixed fonts.
# Type: FontFamily
c.fonts.web.family.fixed = 'Cousine'

# Font family for serif fonts.
# Type: FontFamily
c.fonts.web.family.serif = 'Tinos'

# Font family for sans-serif fonts.
# Type: FontFamily
c.fonts.web.family.sans_serif = 'Arimo'

# Font family for cursive fonts.
# Type: FontFamily
c.fonts.web.family.cursive = None

# Font family for fantasy fonts.
# Type: FontFamily
c.fonts.web.family.fantasy = None

# Default font size (in pixels) for regular text.
# Type: Int
c.fonts.web.size.default = 16

# Default font size (in pixels) for fixed-pitch text.
# Type: Int
c.fonts.web.size.default_fixed = 13

# Bindings for normal mode
config.bind('<', 'tab-move -')
config.bind('<Ctrl+e>', 'open-editor')
config.bind('>', 'tab-move +')
config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')
config.bind('W', 'open -w')
config.bind('e', 'open-editor')
config.bind('zH', 'hint links spawn term "http \'{hint-url}\' | less"')
config.bind('zM', 'hint links spawn mpv --x11-name "mpv-qutebrowser" \'{hint-url}\'')
config.bind('zO', 'hint links spawn term "mimeo \'{hint-url}\'"')
config.bind('zdS', 'hint links spawn term "cd ~/download; svtplay-dl \'{hint-url}\'"')
config.bind('zdY', 'hint links spawn term "cd ~/download; youtube-dl \'{hint-url}\'"')
config.bind('zh', 'spawn term "http \'{url}\' | less"')
config.bind('zm', 'spawn mpv --x11-name "mpv-qutebrowser" \'{url}\'')
config.bind('zo', 'spawn term "mimeo \'{url}\'"')
config.bind('zds', 'spawn term "cd ~/download; svtplay-dl \'{url}\'"')
config.bind('zdy', 'spawn term "cd ~/download; youtube-dl \'{url}\'"')
config.bind('Ä', 'set-cmd-text -s :open -t')
config.bind('Ö', 'set-cmd-text :')
config.bind('ä', 'set-cmd-text -s :open')
config.bind('ö', 'set-cmd-text :')

# Bindings for insert mode
config.bind('<Ctrl+e>', 'open-editor', mode='insert')
