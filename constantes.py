
dbname = 'postgres'
user = 'postgres'
password = 'root'
host = 'localhost'
port = '5433'


QUERY_CLIENTES_ACTIVOS2= "select * from scexamen.personas p join scexamen.usuariosvuelo uv on p.id = uv.idpasajero join scexamen.vuelos v on uv.idvuelo = v.id join scexamen.estado e on e.id = p.estado where upper(e.descripcion) = 'ACTIVO';" #'ACTIVO'
QUERY_DIRECCION = "Select d.calle from scexamen.personas p join scexamen.estado e on e.id = p.estado join scexamen.direccion d on p.iddireccion = d.id where upper(e.descripcion) = 'ACTIVO';"
QUERY_SELECT_VUELO_BY_ID = 'select * from scexamen.personas p join scexamen.usuariosvuelo uv on p.id = uv.idpasajero join scexamen.vuelos v on uv.idvuelo = v.id join scexamen.vuelos c on c.id = v.idciudadorigenwhere v.id = :id;'
