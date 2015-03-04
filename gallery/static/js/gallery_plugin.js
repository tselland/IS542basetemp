/**
 * Created by travisselland on 3/3/15.
 */

(function ( $ ) {
    $.fn.galleryPopOut = function(options){
        console.log("inside plugin");
        options = $.extend(true, {
            css: '/css/gallery.css',
            max_width: 800,
            title_extension: 5

        }, options);

        $(this).children('a').children('img')
            .addClass('gallery_image')
            .each(function(){

            console.log("inside img.each function")

            //create parent div to bind title and image to
            var img_container = $('<div></div>')
                .addClass('img_container');

            // Image label
            var title = $( '<span />' )
                .addClass( 'image_title' )
                .html( $( this ).data( 'title' ) )
                .css({
                    'width': (options.max_width  + (options.title_extension * 2)) + 'px',
                    'margin-left': - (options.title_extension) + 'px'
                });

                //
                // Add elements
                $( this).wrap(img_container).parent()
                        .append( title );



        });

        $( this ).children('a').children('.img_container') //'a').children( '.gallery_image' )
            .hover(
                function(){
                    console.log("hover")
                    // Animate zoom
                    //I decided to use CSS3 transitions instead of the JQuery.animate because I wanted to use
                    //the more standardized way of doing things.
                    //My .animate function would have looked something like this.
                    //$( this ).animate({
                    //    opacity: '0.5',
                    //    height: '250px',
                    //    width: '250px'
                    //},500);
                    $( this ).toggleClass('expanded_image');
                    // Show title label
                    $( this ).children('.image_title').toggleClass('show_title');
                }
            );



        return this;
    };
}( jQuery ));