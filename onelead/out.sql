BEGIN;
CREATE TABLE `leaddb_batch` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(200) NOT NULL,
    `start_date` date NOT NULL,
    `end_date` date NOT NULL,
    `status` varchar(10) NOT NULL,
    `currrent_semester` varchar(10) NOT NULL
)
;
CREATE TABLE `leaddb_student` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `admission_no` varchar(20) NOT NULL,
    `batch_id` integer NOT NULL,
    `name` varchar(200) NOT NULL,
    `gender` varchar(1) NOT NULL,
    `address` varchar(200) NOT NULL,
    `emergency_phone_no` varchar(20) NOT NULL,
    `mobile_no` varchar(20) NOT NULL,
    `email` varchar(50) NOT NULL,
    `parents` varchar(200) NOT NULL,
    `education_history` varchar(200) NOT NULL,
    `admitted_date` date NOT NULL
)
;
ALTER TABLE `leaddb_student` ADD CONSTRAINT `batch_id_refs_id_36d4e40f` FOREIGN KEY (`batch_id`) REFERENCES `leaddb_batch` (`id`);
CREATE TABLE `leaddb_staff` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `emp_no` varchar(20) NOT NULL,
    `name` varchar(200) NOT NULL,
    `gender` varchar(1) NOT NULL,
    `address` varchar(200) NOT NULL,
    `emergency_phone_no` varchar(20) NOT NULL,
    `mobile_no` varchar(20) NOT NULL,
    `email` varchar(50) NOT NULL,
    `education_history` varchar(200) NOT NULL,
    `joined_date` date NOT NULL,
    `emp_type` varchar(20) NOT NULL
)
;
CREATE TABLE `leaddb_subject` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(20) NOT NULL
)
;
CREATE TABLE `leaddb_subjectmap` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `subject_id` integer NOT NULL,
    `batch_id` integer NOT NULL,
    `staff_id` integer NOT NULL
)
;
ALTER TABLE `leaddb_subjectmap` ADD CONSTRAINT `staff_id_refs_id_5d0ca837` FOREIGN KEY (`staff_id`) REFERENCES `leaddb_staff` (`id`);
ALTER TABLE `leaddb_subjectmap` ADD CONSTRAINT `subject_id_refs_id_952b788a` FOREIGN KEY (`subject_id`) REFERENCES `leaddb_subject` (`id`);
ALTER TABLE `leaddb_subjectmap` ADD CONSTRAINT `batch_id_refs_id_9c8cc169` FOREIGN KEY (`batch_id`) REFERENCES `leaddb_batch` (`id`);
CREATE TABLE `leaddb_mentorship` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `student_id` integer NOT NULL,
    `staff_id` integer NOT NULL
)
;
ALTER TABLE `leaddb_mentorship` ADD CONSTRAINT `student_id_refs_id_ca1cf8e4` FOREIGN KEY (`student_id`) REFERENCES `leaddb_student` (`id`);
ALTER TABLE `leaddb_mentorship` ADD CONSTRAINT `staff_id_refs_id_9131fa99` FOREIGN KEY (`staff_id`) REFERENCES `leaddb_staff` (`id`);
CREATE TABLE `leaddb_schedules` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `start_date_time` datetime NOT NULL,
    `end_date_time` datetime NOT NULL,
    `geo_location` varchar(50) NOT NULL,
    `notify` varchar(5) NOT NULL,
    `summary` varchar(200) NOT NULL
)
;
CREATE TABLE `leaddb_eventtypes` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(50) NOT NULL
)
;
CREATE TABLE `leaddb_timetable` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `sub_map_id` integer NOT NULL,
    `start_date_time` datetime NOT NULL,
    `end_date_time` datetime NOT NULL
)
;
ALTER TABLE `leaddb_timetable` ADD CONSTRAINT `sub_map_id_refs_id_7a210997` FOREIGN KEY (`sub_map_id`) REFERENCES `leaddb_subjectmap` (`id`);
CREATE TABLE `leaddb_attendance` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `sub_map_id` integer NOT NULL,
    `student_id` integer NOT NULL,
    `date` date NOT NULL,
    `slot_no` varchar(2) NOT NULL,
    `status_of_student` varchar(10) NOT NULL
)
;
ALTER TABLE `leaddb_attendance` ADD CONSTRAINT `sub_map_id_refs_id_7c7c41c7` FOREIGN KEY (`sub_map_id`) REFERENCES `leaddb_subjectmap` (`id`);
ALTER TABLE `leaddb_attendance` ADD CONSTRAINT `student_id_refs_id_09d1b797` FOREIGN KEY (`student_id`) REFERENCES `leaddb_student` (`id`);

COMMIT;
