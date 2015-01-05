angular.module('attendance', ['ui.bootstrap']);

angular.module('attendance').controller('AttendanceCtrl', function ($scope, $modal, $log) {

  $scope.items = ['item1', 'item2', 'item3'];


});



angular.module('attendance').service('dataService', function () {

    this.liveBatchMapId = null;
    this.getLiveBatchMapId  = function() {
      return this.liveBatchMapId;
    };
    this.setLiveBatchMapId  = function(id){

      this.liveBatchMapId=id;

    };

    this.studentList=null;
    this.getStudentList = function() {
        this.studentList= $http.get('studentlist/'+this.liveBatchMapId);
        return this.studentList;
      };
});


angular.module('attendance').controller('AttendanceInstanceCtrl', function ($scope, $modalInstance,dataService) {

  $scope.liveMapId=dataService.getLiveBatchMapId();
  $scope.students=dataService.getStudentList();
  $scope.ok = function () {
    $modalInstance.close($scope.selected.item);
  };

  $scope.cancel = function () {
    $modalInstance.dismiss('cancel');
  };
});


angular.module('attendance').controller('BatchListCtrl', function ($scope,$http,$modal, $log,dataService) {

  $http.get('batchmaps/1/').success(function(data) {
    $scope.batchMaps = data;
    console.log(data);

  });


  $scope.open = function (id) {


    dataService.setLiveBatchMapId(id);
    var modalInstance = $modal.open({
      templateUrl: 'attendanceModalContent.html',
      controller: 'AttendanceInstanceCtrl',

      resolve: {
        items: function () {
          return $scope.items;
        }
      }
    });

    modalInstance.result.then(function (selectedItem) {
      $scope.selected = selectedItem;
    }, function () {
      $log.info('Modal dismissed at: ' + new Date());
    });
  };
});

angular.module('attendance').controller('StudentListCtrl', function ($scope,$http,$modal, $log,dataService) {

  $http.get('studentlist/1/').success(function(data) {
    $scope.batchMaps = data;
    console.log(data);

  });
});


angular.module('attendance').controller('DatepickerCtrl', function ($scope) {
  $scope.today = function() {
    $scope.dt = new Date();
  };
  $scope.today();

  $scope.clear = function () {
    $scope.dt = null;
  };
 $scope.open = function($event) {
    $event.preventDefault();
    $event.stopPropagation();

    $scope.opened = true;
  };

  $scope.dateOptions = {
    formatYear: 'yy',
    startingDay: 1
  };

  $scope.format='dd-MM-yy';

});


angular.module('attendance').controller('ButtonsCtrl', function ($scope) {
  $scope.singleModel = 1;

  $scope.radioModel = 'Middle';

  $scope.checkModel = {
    left: false,
    middle: true,
    right: false
  };
});
