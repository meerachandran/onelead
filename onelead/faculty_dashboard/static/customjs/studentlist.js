angular.module.factory('studentListService', function($http) {
   return {
     getStudentList: function(callback) {
       $http.get('http://localhost:8000/faculty/studentlist/1/').success(callback);
     }
   }
});
