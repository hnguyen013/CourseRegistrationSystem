# Course Registration System

## 1. Giới thiệu

Course Registration System là ứng dụng quản lý đăng ký học phần được xây dựng bằng Python. Ứng dụng sử dụng giao diện đồ họa GUI Tkinter và cơ sở dữ liệu SQLite để quản lý sinh viên, giảng viên, học phần, đăng ký học phần và báo cáo thống kê.

---

## 2. Công nghệ sử dụng

* Python
* Tkinter
* ttk.Treeview
* SQLite
* CSV
* Git/GitHub

---

## 3. Chức năng chính

### Dashboard

* Hiển thị giao diện chính của hệ thống.
* Có sidebar để chuyển sang các trang:

  * Student
  * Lecturer
  * Course
  * Registration
  * Reports
* Có các thẻ chức năng để mở nhanh từng module.

### Student Management

* Thêm sinh viên.
* Cập nhật thông tin sinh viên.
* Xóa sinh viên.
* Tìm kiếm sinh viên theo mã, tên hoặc ngành học.
* Hiển thị danh sách sinh viên bằng bảng Treeview.

### Lecturer Management

* Thêm giảng viên.
* Cập nhật thông tin giảng viên.
* Xóa giảng viên.
* Hiển thị danh sách giảng viên.

### Course Management

* Thêm học phần.
* Cập nhật học phần.
* Xóa học phần.
* Hiển thị danh sách học phần.
* Phân loại học phần thành:

  * Compulsory Course
  * Elective Course

### Registration Management

* Đăng ký học phần cho sinh viên.
* Kiểm tra sinh viên có tồn tại hay không.
* Kiểm tra học phần có tồn tại hay không.
* Kiểm tra trùng đăng ký.
* Hiển thị danh sách đăng ký học phần.
* Tính tổng học phí của sinh viên.

### Reports

* Thống kê học phí theo từng sinh viên.
* Thống kê số lượng sinh viên đăng ký theo từng học phần.
* Xuất báo cáo ra file CSV trong thư mục `exports`.

---

## 4. Cấu trúc thư mục

```text
CourseRegistrationSystem/
│
├── main.py
│
├── database/
│   └── course_registration.db
│
├── exports/
│   └── report.csv
│
├── models/
│   ├── person.py
│   ├── student.py
│   ├── lecturer.py
│   ├── course.py
│   ├── compulsory_course.py
│   └── elective_course.py
│
├── services/
│   ├── database_service.py
│   ├── student_service.py
│   ├── lecturer_service.py
│   ├── course_service.py
│   └── registration_service.py
│
└── views/
    ├── base_view.py
    ├── dashboard_view.py
    ├── student_view.py
    ├── lecturer_view.py
    ├── course_view.py
    ├── registration_view.py
    ├── report_view.py
    └── style.py
```

---

## 5. Kiến trúc hệ thống

Dự án được chia theo mô hình phân tầng:

### models

Chứa các lớp đối tượng của hệ thống:

* Person
* Student
* Lecturer
* Course
* CompulsoryCourse
* ElectiveCourse

### services

Chứa phần xử lý dữ liệu và nghiệp vụ:

* Kết nối SQLite.
* Thêm, sửa, xóa, lấy dữ liệu.
* Xử lý đăng ký học phần.
* Tính tổng học phí.

### views

Chứa giao diện người dùng:

* Dashboard
* Student Management
* Lecturer Management
* Course Management
* Registration Management
* Reports

---

## 6. Cơ sở dữ liệu

Ứng dụng sử dụng SQLite với file:

```text
database/course_registration.db
```

Các bảng chính:

### students

Lưu thông tin sinh viên:

* student_id
* name
* email
* major

### lecturers

Lưu thông tin giảng viên:

* lecturer_id
* name
* email
* department

### courses

Lưu thông tin học phần:

* course_id
* course_name
* credits
* tuition_fee
* course_type

### registrations

Lưu thông tin đăng ký học phần:

* registration_id
* student_id
* course_id
* registration_date

---

## 7. Áp dụng lập trình hướng đối tượng

### Inheritance

Dự án có sử dụng kế thừa.

Lớp `Person` là lớp cha của:

* `Student`
* `Lecturer`

Lớp `Course` là lớp cha của:

* `CompulsoryCourse`
* `ElectiveCourse`

### Encapsulation

Các thông tin của đối tượng được quản lý thông qua class trong thư mục `models`.
Tuy nhiên, phiên bản hiện tại chưa dùng thuộc tính private dạng `__attribute`.

### Polymorphism

Dự án đã có cấu trúc lớp cha - lớp con cho Course, CompulsoryCourse và ElectiveCourse.
Tuy nhiên, phiên bản hiện tại chưa có phương thức được override rõ ràng giữa các lớp con.

### Abstraction

Phiên bản hiện tại chưa sử dụng Abstract Base Class hoặc Interface.

---

## 8. Hướng dẫn chạy chương trình

### Bước 1: Mở thư mục project

```bash
cd CourseRegistrationSystem
```

### Bước 2: Chạy chương trình

```bash
python main.py
```

Sau khi chạy, chương trình sẽ tự tạo các bảng trong cơ sở dữ liệu nếu chưa tồn tại.

---

## 9. Mapping to Assignment Requirements

| Yêu cầu                   | Tình trạng trong project                                                                                     |
| ------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Encapsulation             | Có tổ chức dữ liệu bằng class, nhưng chưa dùng private attribute `__attribute`.                              |
| Inheritance               | Đã có. `Student` và `Lecturer` kế thừa `Person`; `CompulsoryCourse` và `ElectiveCourse` kế thừa `Course`.    |
| Polymorphism              | Chưa thể hiện rõ vì các lớp con chưa override phương thức riêng.                                             |
| Abstraction               | Chưa có Abstract Base Class hoặc Interface.                                                                  |
| Layered Architecture      | Đã có. Project chia thành `models`, `services`, `views`.                                                     |
| Clean Code                | Code được chia theo từng file, từng chức năng riêng.                                                         |
| Exception Handling        | Có xử lý lỗi trong một số service và view, ví dụ lỗi trùng ID, lỗi nhập credits/tuition fee.                 |
| CRUD                      | Đã có CRUD cho Student, Lecturer, Course. Registration có thêm và hiển thị danh sách.                        |
| Search & Sort             | Đã có tìm kiếm Student. Chưa có sort rõ ràng.                                                                |
| Permanent Storage         | Đã có lưu trữ bằng SQLite.                                                                                   |
| Complex Transaction Logic | Đã có logic đăng ký học phần: kiểm tra sinh viên, kiểm tra học phần, kiểm tra trùng đăng ký và tính học phí. |
| Statistics & Reports      | Đã có báo cáo học phí sinh viên, báo cáo số lượng đăng ký theo học phần và xuất CSV.                         |
| Advanced Technology       | Đã có GUI bằng Tkinter và SQLite Database.                                                                   |
| Git & GitHub              | Project có thư mục `.git`; cần đẩy lên GitHub và bổ sung link repository khi nộp.                            |

---

## 10. Kết quả đạt được

* Xây dựng được ứng dụng quản lý đăng ký học phần bằng Python.
* Có giao diện GUI bằng Tkinter.
* Có cơ sở dữ liệu SQLite.
* Có các chức năng quản lý sinh viên, giảng viên, học phần và đăng ký học phần.
* Có báo cáo thống kê và xuất file CSV.
* Có cấu trúc phân tầng rõ ràng.

---

## 11. Hướng phát triển thêm

Để project đáp ứng tốt hơn yêu cầu chấm điểm, có thể bổ sung:

* Thêm private attribute và getter/setter cho các model.
* Thêm Abstract Base Class.
* Thêm phương thức override trong `CompulsoryCourse` và `ElectiveCourse`.
* Thêm chức năng sort cho các bảng.
* Thêm chức năng xóa đăng ký học phần trên giao diện.
* Thêm kiểm tra dữ liệu nhập cho Student và Lecturer.
* Bổ sung ảnh giao diện vào README.

---

## 12. Thành viên thực hiện

Họ và tên: Trần Hạnh Nguyên

Lớp: Tin 2E

Môn học: Programming Methods

Giảng viên hướng dẫn: ThS. Trần Văn Long
