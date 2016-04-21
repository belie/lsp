(function (angular) {
    'use strict';

    var resultsApp = angular.module('ResultsApp', []);

    resultsApp.controller('ResultsController', function($http, $scope) {

        $http.get("/lsp/qa_status").then(function(response) {

            $scope.qaResultsData = response.data;

        });

    });

})(angular);
