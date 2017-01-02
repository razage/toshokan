define([
  'jquery',
  'backbone',
  'views/forms/addSeries',
  'bootstrap'
], function($, Backbone, AddSeriesView) {
    var v = new AddSeriesView();

    var TopbarView = Backbone.View.extend({
        el: ".topbar ul.nav",

        events: {
            "click .add": "addSeries"
        },

        initialize: function() {
            console.log("Topbar initialized");
        },

        addSeries: function(e) {
            e.preventDefault();
            v.render();

            $(".viewbox").slideToggle(300, function() {
//                if ($(".content").css("opacity") == 0.6) {
//                    $(".content").css({opacity: 1});
//                    $(e.currentTarget).removeClass("active");
//                }
//                else {
//                    $(".content").css({opacity: 0.6});
//                    $(e.currentTarget).addClass("active");
//                }
            });
        }
    });

    return TopbarView;
});