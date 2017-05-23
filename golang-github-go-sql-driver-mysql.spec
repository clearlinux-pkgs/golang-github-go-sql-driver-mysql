Name     : golang-github-go-sql-driver-mysql 
Version  : 1.2
Release  : 9
URL      : https://github.com/go-sql-driver/mysql/archive/v1.2.tar.gz
Source0  : https://github.com/go-sql-driver/mysql/archive/v1.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MPL-2.0
BuildRequires : go

%description
# Go-MySQL-Driver
A MySQL-Driver for Go's [database/sql](http://golang.org/pkg/database/sql) package

%prep
%setup -q -n mysql-1.2

%build

%install
%global gopath /usr/lib/golang
%global library_path github.com/go-sql-driver/mysql 
rm -rf %{buildroot}
# Copy all *.go and *.s files
install -d -p %{buildroot}%{gopath}/src/%{library_path}/
for ext in go s; do
    for file in $(find . -iname "*.$ext") ; do
         install -d -p %{buildroot}%{gopath}/src/%{library_path}/$(dirname $file)
         cp -pav $file %{buildroot}%{gopath}/src/%{library_path}/$file
    done
done

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export GOPATH=%{buildroot}%{gopath}
go test %{library_path}

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/go-sql-driver/mysql/appengine.go
/usr/lib/golang/src/github.com/go-sql-driver/mysql/benchmark_test.go
/usr/lib/golang/src/github.com/go-sql-driver/mysql/buffer.go
/usr/lib/golang/src/github.com/go-sql-driver/mysql/collations.go
/usr/lib/golang/src/github.com/go-sql-driver/mysql/connection.go
/usr/lib/golang/src/github.com/go-sql-driver/mysql/const.go
/usr/lib/golang/src/github.com/go-sql-driver/mysql/driver.go
/usr/lib/golang/src/github.com/go-sql-driver/mysql/driver_test.go
/usr/lib/golang/src/github.com/go-sql-driver/mysql/errors.go
/usr/lib/golang/src/github.com/go-sql-driver/mysql/errors_test.go
/usr/lib/golang/src/github.com/go-sql-driver/mysql/infile.go
/usr/lib/golang/src/github.com/go-sql-driver/mysql/packets.go
/usr/lib/golang/src/github.com/go-sql-driver/mysql/result.go
/usr/lib/golang/src/github.com/go-sql-driver/mysql/rows.go
/usr/lib/golang/src/github.com/go-sql-driver/mysql/statement.go
/usr/lib/golang/src/github.com/go-sql-driver/mysql/transaction.go
/usr/lib/golang/src/github.com/go-sql-driver/mysql/utils.go
/usr/lib/golang/src/github.com/go-sql-driver/mysql/utils_test.go
