Commands
========

All sioyek keybindings execute some command. You can open a searchable list of all sioyek commands by pressing :code:`:` by default.
Below is a list of all available sioyek commands.


:code:`goto_begining`
^^^^^^^^^^^^^^^^^^^^^
Go to the beginning of the document. If prefixed with a number, it will go to that page number.

:code:`goto_end`
^^^^^^^^^^^^^^^^
Go to the end of the document. If prefixed with a number, it will go to that page number.

:code:`goto_definition`
^^^^^^^^^^^^^^^^^^^^^^^
While the visual ruler is highlighting a line, executing :code:`goto_definition` will jump to the location of reference in that line. For example,
executing this command while a line containing "Figure 2.1" is highlighted will jump to the location of the figure in the document.

:code:`overview_definition`
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Similar to :code:`goto_definition`, but instead of jumping to the location of the reference, it will show a small overview of the reference in the
overview window.

:code:`portal_to_definition`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Similar to :code:`goto_definition`, but instead of jumping to the location of the reference, it will create a portal from current location to the
location of the definition.


:code:`next_item`
^^^^^^^^^^^^^^^^^
While a search is in progress, this command will jump to the next search result.

:code:`previous_item`
^^^^^^^^^^^^^^^^^^^^^
While a search is in progress, this command will jump to the previous search result.

:code:`set_mark`
^^^^^^^^^^^^^^^^
Mark the location with the symbol entered following the :code:`set_mark` command.

:code:`goto_mark`
^^^^^^^^^^^^^^^^^
Go to the mark previously set using :code:`set_mark`.

:code:`goto_page_with_page_number`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Go to the page number corresponding to entered text.

:code:`search`
^^^^^^^^^^^^^^
Search for a text in document.

:code:`regex_search`
^^^^^^^^^^^^^^^^^^^^
Search for a regular expression in the document.

:code:`move_down`, :code:`move_up`, :code:`move_left`, :code:`move_right`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Move the document.

:code:`zoom_in` and :code:`zoom_out`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Change the zoom level.

:code:`fit_to_page_width` and :code:`fit_to_page_height`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Fit the current page to window width/height.

:code:`fit_to_page_width_smart` and :code:`fit_to_page_height_smart`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Fit the current page (ignoring white margins) to window width/height.

:code:`next_page` and :code:`previous_page`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Navigate to the next/previous page.

:code:`open_document`
^^^^^^^^^^^^^^^^^^^^^
Open the file browser to open a document.

:code:`add_bookmark`
^^^^^^^^^^^^^^^^^^^^
Add a bookmark to the current location at the document with the entered text. 

:code:`add_highlight`
^^^^^^^^^^^^^^^^^^^^^
Add the selected text as a highlight with the type of following symbol.

:code:`goto_toc`
^^^^^^^^^^^^^^^^
Open the table of contents.

:code:`goto_bookmark`
^^^^^^^^^^^^^^^^^^^^^
Open bookmark list of current document.

:code:`goto_highlight`
^^^^^^^^^^^^^^^^^^^^^^
Open highlight list of current document.

:code:`goto_bookmark_g`
^^^^^^^^^^^^^^^^^^^^^^^
Open bookmark list of all documents.

:code:`goto_highlight_g`
^^^^^^^^^^^^^^^^^^^^^^^^
Open highlight list of all documents.

:code:`portal`
^^^^^^^^^^^^^^
Set the current location as the portal source. If a portal source is already set, then use the current
location as the portal destination and create the portal.

:code:`next_state`, :code:`prev_state`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Go forward/backward in history.

:code:`delete_bookmark`
^^^^^^^^^^^^^^^^^^^^^^^
Delete the closest bookmark to the current location.

:code:`delete_highlight`
^^^^^^^^^^^^^^^^^^^^^^^^
Delete the last highlight clicked on.

:code:`delete_portal`
^^^^^^^^^^^^^^^^^^^^^
Delete the closest portal to the current location.

:code:`goto_portal`
^^^^^^^^^^^^^^^^^^^
Go to the destination of the closest portal source to the current document location.

:code:`edit_portal`
^^^^^^^^^^^^^^^^^^^
Jump to the destination of the closest portal. All the edits you do to the location/zoom is applied to the portal
when you go back by executing :code:`prev_state`.

:code:`open_prev_doc`
^^^^^^^^^^^^^^^^^^^^^
Open a list of all opened document using sioyek.

:code:`open_document_embedded`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Open an embedded file browser in sioyek.

:code:`open_document_embedded_from_current_path`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Open an embedded file browser in sioyek. Initially, we are in the directory of current document.

:code:`copy`
^^^^^^^^^^^^
Copy the selected text into clipboard.

:code:`toggle_fullscreen`
^^^^^^^^^^^^^^^^^^^^^^^^^
Toggle fullscreen mode.

:code:`toggle_one_window`
^^^^^^^^^^^^^^^^^^^^^^^^^
Open/close the helper window.

:code:`toggle_highlight`
^^^^^^^^^^^^^^^^^^^^^^^^
Toggle whether we highlight PDF links.

:code:`toggle_synctex`
^^^^^^^^^^^^^^^^^^^^^^
Toggle synctex mode. In synctex mode, right clicking on a PDF file opens the corresponding location in the latex file
using the configured text editor.

:code:`command`
^^^^^^^^^^^^^^^
Open a list of all sioyek commands.

:code:`external_search`
^^^^^^^^^^^^^^^^^^^^^^^
Search the selected text in the extenal search engine corresponding to the following symbol.

:code:`open_selected_url`
^^^^^^^^^^^^^^^^^^^^^^^^^
Open the selected URL in a browser.

:code:`screen_up` and :code:`screen_down`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Move the screen up/down.

:code:`next_chapter` and :code:`prev_chapter`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Go to the next/previous chapter in the current document.

:code:`toggle_dark_mode`
^^^^^^^^^^^^^^^^^^^^^^^^
Switch between light/dark colorschemes.

:code:`toggle_presentation_mode`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Toggle presentation mode. In presentation mode we only show one page at a time and the current page
fills the entire window.

:code:`toggle_mouse_drag_mode`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Toggle mouse drag mode. In mouse drag mode, clicking and dragging using mouse moves the document (instead of selecting text).

:code:`close_window`
^^^^^^^^^^^^^^^^^^^^
Close the current window.

:code:`quit` and :code:`q`
^^^^^^^^^^^^^^^^^^^^^^^^^^
Quit sioyek (closes all windows).

:code:`open_link`
^^^^^^^^^^^^^^^^^
Open the PDF links using keyboard. Each link will be shown with a label and the link corresponding to the entered label text will be opened.

:code:`keyboard_select`
^^^^^^^^^^^^^^^^^^^^^^^
Select text using keyboard. Each word in the document will be shown with a label. You should enter the labels corresponding to the
beginning and end of the selection (separated by a space).

:code:`keyboard_smart_jump` and :code:`keyboard_overview`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Perform a smartjump (or open an overview) using keyboard. Each word in the document will be shown with a label and we will smart jump to the location of the
reference corresponding to the entered label.

:code:`keys` and :code:`prefs`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Open the :code:`keys.config` / :code:`prefs.config` file.

:code:`keys_user` and :code:`prefs_user`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Open the :code:`keys_user.config` / :code:`prefs_user.config` file.

:code:`export` and :code:`import`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Export/import sioyek data to/from a json file.

:code:`enter_visual_mark_mode`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Place a visual mark at the center of screen.

:code:`move_visual_mark_down` and :code:`move_visual_mark_up`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Move the visual mark up and down which highlights the previous/next line.

:code:`toggle_visual_scroll`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Toggle visual scroll mode. In visual scroll mode, mouse wheel moves the ruler (the visual mark) instead of scrolling the document.

:code:`toggle_horizontal_scroll_lock`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Toggles the horizontal scroll lock which prevents scrolling in horizontal direction (useful for touchpad users).

:code:`toggle_custom_color`
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Toggle custom color mode. In this mode, we change the text/background color of the document to the colors specified in :code:`prefs_user.config`.

:code:`execute`
^^^^^^^^^^^^^^^
Execute the entered text as a shell command.

:code:`execute_predefined_command`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Execute the predefined command (in :code:`prefs_user.config`) corresponding to the following symbol.

:code:`embed_annotations`
^^^^^^^^^^^^^^^^^^^^^^^^^
Export a new version of the current document with all sioyek annotations embedded so that they are visible in other software.

:code:`copy_window_size_config`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Copy the current window size configuration (useful when you want to set the configs in :code:`prefs_user.config`).


:code:`toggle_select_highlight`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Toggle select highlight mode. In this mode, just selecting the text automatically highlights it.

:code:`set_select_highlight_type`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Set the highlight type used in select highlight mode.

:code:`open_last_document`
^^^^^^^^^^^^^^^^^^^^^^^^^^
Open the previous document.

:code:`toggle_window_configuration`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Toggle between one window/two window configuration settings.

:code:`prefs_user_all` and :code:`keys_user_all`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Show a list of all :code:`prefs_user.config` / :code:`keys_user.config` files discovered by sioyek.

:code:`fit_to_page_width_ratio`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Similar to :code:`fit_to_page_width`  but instead of fitting to the entire screen width, we fit to a ratio configured in
:code:`prefs_user.config`.

:code:`smart_jump_under_cursor` and :code:`overview_under_cursor`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Perform a smart jump (or open an overview) to the reference under the mouse cursor.

:code:`close_overview`
^^^^^^^^^^^^^^^^^^^^^^
Close the overview window.

:code:`visual_mark_under_cursor`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Place a visual mark (ruler) under the mouse cursor.

:code:`close_visual_mark`
^^^^^^^^^^^^^^^^^^^^^^^^^
Exit the visual mark (ruler) mode.

:code:`zoom_in_cursor` and :code:`zoom_out_cursor`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Zoom in/out on the mouse cursor.

:code:`goto_left`, :code:`goto_right`, :code:`goto_top_of_page` and :code:`goto_bottom_of_page`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Go to the left/right/top/bottom of the current page.

:code:`goto_left_smart` and :code:`goto_right_smart`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Go to the left/right side of the current page ignoring white margins.

:code:`rotate_clockwise` and :code:`rotate_counterclockwise`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Rotate the document.

:code:`goto_next_highlight` and :code:`goto_prev_highlight`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Go to the next/previous highlight in the current document.

:code:`goto_next_highlight_of_type` and :code:`goto_prev_highlight_of_type`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Go to the next/previous highlight in the current document with following symbol's type.

:code:`add_highlight_with_current_type`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Add a highlight with the type specified using :code:`set_select_highlight_type`.

:code:`enter_password`
^^^^^^^^^^^^^^^^^^^^^^
Enter the password for password-protected documents.

:code:`toggle_fastread`
^^^^^^^^^^^^^^^^^^^^^^^
Highlight the first few characters of each word. Supposedly it may increase reading speed (unconfirmed).

:code:`new_window`
^^^^^^^^^^^^^^^^^^
Open a new sioyek window.

:code:`toggle_statusbar`
^^^^^^^^^^^^^^^^^^^^^^^^
Toggle the statusbar at the bottom of the screen.

:code:`reload`
^^^^^^^^^^^^^^
Reload the current document.

:code:`synctex_under_cursor`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Perform a synctex search for the location under mouse cursor.

:code:`set_status_string`
^^^^^^^^^^^^^^^^^^^^^^^^^
Set a message to be displayed in sioyek's statusbar.

:code:`clear_status_string`
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Clear the message in sioyek's statusbar.

:code:`toggle_titlebar`
^^^^^^^^^^^^^^^^^^^^^^^
Toggle the window titlebar.

:code:`next_preview` and :code:`previous_preview`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If there are multiple possible previews for the overview window, move to the next/previous preview.

:code:`goto_overview` and :code:`portal_to_overview`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Go to / create a portal to the location displayed in the overview window.

:code:`goto_selected_text`
^^^^^^^^^^^^^^^^^^^^^^^^^^
Jump to the location of current selected text.

:code:`focus_text`
^^^^^^^^^^^^^^^^^^
If in visual mark (ruler) mode, focus the ruler on the line corresponding to the entered text.

:code:`goto_window`
^^^^^^^^^^^^^^^^^^^
Open a searchable list of sioyek windows.

:code:`toggle_smooth_scroll_mode`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Toggle smooth scroll mode. In this mode, scrolling is done smoothly.

:code:`toggle_scrollbar`
^^^^^^^^^^^^^^^^^^^^^^^^
Toggle the scrollbar.

:code:`overview_to_portal`
^^^^^^^^^^^^^^^^^^^^^^^^^^
Open the overview window to the closest portal to current document location.

:code:`select_rect`
^^^^^^^^^^^^^^^^^^^

Select a rectangle (can be used in extensions using :code:`%{selected_rectangle}` variable).

:code:`donate`
^^^^^^^^^^^^^^

Open donation page.

:code:`overview_next_item` and :code:`overview_prev_item`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open overviews to previous/next search items.