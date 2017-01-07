define([
  'backbone',
  'models/series'
], function(Backbone, SeriesModel) {
    var SeriesList = Backbone.Collection.extend({
        model: SeriesModel,
        url: "/series"
    });

    return SeriesList;
});