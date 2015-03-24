/**
 * @license Copyright (c) 2003-2013, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see LICENSE.html or http://ckeditor.com/license
 */

CKEDITOR.editorConfig = function( config ) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
    config.extraPlugins = 'oembed,widget,leaflet,codesnippet';

    config.oembed_maxWidth = '715';
    config.oembed_WrapperClass = 'flex-video';

    config.codeSnippet_theme = 'sunburst';

    config.allowedContent = true;
};
