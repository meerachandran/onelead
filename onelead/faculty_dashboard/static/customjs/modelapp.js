angular.module('attendance', ['ui.bootstrap']);
angular.module('attendance').controller('AttendanceCtrl', function ($scope, $modal, $log) {

  $scope.items = ['item1', 'item2', 'item3'];


});

// Please note that $modalInstance represents a modal window (instance) dependency.
// It is not the same as the $modal service used above.

angular.module('attendance').controller('AttendanceInstanceCtrl', function ($scope, $modalInstance, items) {



  $scope.ok = function () {
    $modalInstance.close($scope.selected.item);
  };

  $scope.cancel = function () {
    $modalInstance.dismiss('cancel');
  };
});


angular.module('attendance').controller('BatchListCtrl', function ($scope,$http,$modal, $log) {

  $http.get('batchmaps/1/').success(function(data) {
    $scope.batchMaps = data;
    console.log(data);

  });


  $scope.open = function (id) {


    console.log($scope.liveMapId);
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

angular.module('attendance').controller('StudentListCtrl', function ($scope,$http,$modal, $log) {

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
