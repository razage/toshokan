define([
  'jquery',
  'backbone',
  'collections/seriesList',
  'models/series',
  'models/volume',
  'hbs!templates/series/seriesList',
  'hbs!templates/series/seriesView',
  'hbs!templates/series/chapterView',
  'bootstrap',
  'slimscroll'
], function($, Backbone, SeriesList, SeriesModel, VolumeModel, SeriesListTemplate, SeriesViewTemplate, ChapterViewTemplate) {
    var MainRouter = Backbone.Router.extend({
        routes: {
            "library": "seriesList",
            "library/:sid": "seriesIndex",
            "library/:sid/:vid": "volumeIndex"
        },

        $el: $(".content"),

        slimScrollRefresh: function() {
            $(".scroll").slimScroll({
                railColor: "#4C5A69",
                color: "#0EAC51",
                railVisible: true,
                height: "auto"
            });
        },

        seriesList: function() {
            var s = new SeriesList(),
                that = this;

            s.fetch({
                success: function(model, response, options) {
                    var slt = SeriesListTemplate(s);
                    that.$el.html(slt);
                    that.slimScrollRefresh();
                }
            });
        },

        seriesIndex: function(sid) {
            var s = new SeriesModel({collection: SeriesList, id: sid}),
                that = this;

            s.fetch({
                success: function(model, response, options) {
                    s.hasDoujins = (model.get("doujins").length < 1) ? false : true;
                    s.hasVolumes = (model.get("volumes").length < 1) ? false : true;

                    var svt = SeriesViewTemplate(s);
                    that.$el.html(svt);
                    that.slimScrollRefresh();
                }
            });
        },

        volumeIndex: function(sid, vid) {
            var v = new VolumeModel({id: vid, sid: sid}),
                that = this;

            v.fetch({
                success: function(model, response, options) {
                    var cvt = ChapterViewTemplate(v);
                    that.$el.html(cvt);
                    that.slimScrollRefresh();
                }
            });
        }
    });

    return MainRouter;
});
