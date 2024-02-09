odoo.define('algolia_search_integration.search_integration', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    var core = require('web.core');
    var Widget = require('web.Widget');

    var QWeb = core.qweb;
    var _t = core._t;

    var AlgoliaSearchWidget = Widget.extend({
        template: 'algolia_search_integration.search_template',
        xmlDependencies: ['/static/src/xml/search_templates.xml'],
        events: {
            'input .searchInput': 'handleSearchInput',
        },

        init: function (parent, options) {
            this._super(parent);
            this.algoliaClient = options.algoliaClient;
            this.searchIndex = this.algoliaClient.initIndex('product.index');
        },

        start: function () {
            this.$searchInput = this.$('.searchInput');
            this.$searchResultsContainer = this.$('.searchResultsContainer');
            this.$searchFilterOptions = this.$('.searchFilterOptions');
            return this._super.apply(this, arguments);
        },

        handleSearchInput: function () {
            var self = this;
            var query = this.$searchInput.val();
            this.searchIndex.search(query, {
                hitsPerPage: 10,
                facets: '*',
                facetFilters: this.getFacetFilters()
            }).then(function (responses) {
                self.updateSearchResults(responses.hits);
            });
        },

        getFacetFilters: function () {
            // Collect facet filters from the searchFilterOptions
            var filters = [];
            this.$searchFilterOptions.find('input:checked').each(function () {
                filters.push($(this).data('filter'));
            });
            return filters;
        },

        updateSearchResults: function (hits) {
            var htmlContent = QWeb.render('algolia_search_integration.search_results', {
                hits: hits
            });
            this.$searchResultsContainer.html(htmlContent);
        },
    });

    function initAlgoliaSearch() {
        var algoliaClient = algoliasearch('YourApplicationID', 'YourSearchOnlyAPIKey');
        var searchWidget = new AlgoliaSearchWidget(this, {
            algoliaClient: algoliaClient
        });
        searchWidget.appendTo($('.o_web_client'));
    }

    core.action_registry.add('algolia_search_integration.action', AlgoliaSearchWidget);

    return {
        AlgoliaSearchWidget: AlgoliaSearchWidget,
        initAlgoliaSearch: initAlgoliaSearch,
    };
});