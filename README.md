migrationlar bozulduğu için burada durduruyorum, bir sonraki sessionda bunun migrationlarını düzenleyip
querysetten veri çekebilen bir select field haline getireceğim, bu sayede objeyi instance olarak render
ettiğimde multiple select fieldda string olarak veri alabiliyor olacağım, bu da hem daha human readable
hem de mail backend'in ilk adımı olacak. isimler bu şekilde düzgün kaydedildiğinden  LDAP kurulumunda
yük hafiflemiş olacak

------------------------------------
18.12.23 güncelleme

ModelMultipleChoiceField Kullanarak bir querysetten çoklu seçim yapmayı ve bunları tekrardan bir instance'la update etmeyi ekleyebildim. bu sayede ana projedeki büyük veri tabanını kullanarak bir choice field'la ilgilenebileceğim. hem de artık bir tupple değil de bir set sahibi olduğum için instance ekranında hali hazırda seçilmiş objeler geri geliyor.
