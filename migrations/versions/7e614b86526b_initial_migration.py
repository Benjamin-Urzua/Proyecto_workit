"""Initial migration.

Revision ID: 7e614b86526b
Revises: 
Create Date: 2022-06-09 15:56:54.343145

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7e614b86526b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_trabajo')
    op.drop_table('tb_provincia')
    op.drop_table('tb_fotostrabajos')
    op.drop_index('detalleOrdenServicio_rubro', table_name='tb_detalleordenservicio')
    op.drop_index('trabajosEspecialista_detalleOrdenServicio', table_name='tb_detalleordenservicio')
    op.drop_table('tb_detalleordenservicio')
    op.drop_table('tb_especialista')
    op.drop_table('tb_rubro')
    op.drop_index('comuna_direccion', table_name='tb_direccion')
    op.drop_table('tb_direccion')
    op.drop_table('tb_estadotrabajo')
    op.drop_table('tb_trabajadormes')
    op.drop_table('tb_region')
    op.drop_index('direccion_cliente', table_name='tb_cliente')
    op.drop_index('respuestaSeguridad_cliente', table_name='tb_cliente')
    op.drop_table('tb_cliente')
    op.drop_table('tb_trabajosespecialista')
    op.drop_table('tb_perfilcliente')
    op.drop_table('tb_profesion')
    op.drop_table('tb_reporte')
    op.drop_table('tb_perfilespecialista')
    op.drop_table('tb_resena')
    op.drop_table('tb_preguntasseguridad')
    op.drop_table('tb_respuestaseguridad')
    op.drop_index('provincia_comuna', table_name='tb_comuna')
    op.drop_table('tb_comuna')
    op.drop_table('tb_ordenservicio')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_ordenservicio',
    sa.Column('codOrdenServicio', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('nombreServicio', mysql.VARCHAR(length=60), nullable=False),
    sa.Column('runCliente', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('runEspecialista', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('fechaInicio', sa.DATE(), nullable=False),
    sa.Column('fechaFin', sa.DATE(), nullable=False),
    sa.Column('codDireccion', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('descripción', mysql.VARCHAR(length=500), nullable=False),
    sa.Column('codDetalleOrden', mysql.INTEGER(), autoincrement=False, nullable=False),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('tb_comuna',
    sa.Column('codComuna', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('nombreComuna', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('codProvincia', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('codComuna'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('provincia_comuna', 'tb_comuna', ['codProvincia'], unique=False)
    op.create_table('tb_respuestaseguridad',
    sa.Column('codRespuesta', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('codPregunta', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('respuesta', mysql.VARCHAR(length=200), nullable=False),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('tb_preguntasseguridad',
    sa.Column('codPregunta', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('pregunta', mysql.VARCHAR(length=200), nullable=False),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('tb_resena',
    sa.Column('codResena', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('runCliente', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=10), nullable=False),
    sa.Column('runEspecialista', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=10), nullable=False),
    sa.Column('resena', mysql.VARCHAR(length=1000), nullable=False),
    sa.Column('calificacion', mysql.INTEGER(), autoincrement=False, nullable=False),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('tb_perfilespecialista',
    sa.Column('codPerfilEsp', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('runEspecialista', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('codTrabajoEspecialista', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('descripcionPersonal', mysql.VARCHAR(length=500), nullable=False),
    sa.Column('codServicios', mysql.INTEGER(), autoincrement=False, nullable=False),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('tb_reporte',
    sa.Column('codReporte', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('runEspecialista', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=10), nullable=False),
    sa.Column('runCliente', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=10), nullable=False),
    sa.Column('motivo', mysql.VARCHAR(length=300), nullable=False),
    sa.Column('prueba', mysql.VARCHAR(length=500), nullable=False),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('tb_profesion',
    sa.Column('codProfesion', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('nombreProfesion', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('codRubro', mysql.INTEGER(), autoincrement=False, nullable=False),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('tb_perfilcliente',
    sa.Column('codPerfilCli', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('descripcion', mysql.VARCHAR(length=500), nullable=False),
    sa.Column('runCliente', mysql.VARCHAR(length=10), nullable=False),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('tb_trabajosespecialista',
    sa.Column('codTrabajoEspecialista', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('nombreTrabajo', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('valorTrabajo', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('descripcionTrabajo', mysql.VARCHAR(length=400), nullable=False),
    sa.Column('codFotosTrabajos', mysql.INTEGER(), autoincrement=False, nullable=False),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('tb_cliente',
    sa.Column('run', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('nombres', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('apellidos', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('telefono', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('correo', mysql.VARCHAR(length=60), nullable=False),
    sa.Column('contrasena', mysql.VARCHAR(length=60), nullable=False),
    sa.Column('codDireccion', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('codRespuesta', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('fechaNacto', sa.DATE(), nullable=False),
    sa.Column('fotoPerfil', mysql.VARCHAR(length=2000), nullable=False),
    sa.PrimaryKeyConstraint('run'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('respuestaSeguridad_cliente', 'tb_cliente', ['codRespuesta'], unique=False)
    op.create_index('direccion_cliente', 'tb_cliente', ['codDireccion'], unique=False)
    op.create_table('tb_region',
    sa.Column('codRegion', mysql.VARCHAR(length=4), nullable=False),
    sa.Column('nombreRegion', mysql.VARCHAR(length=100), nullable=False),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('tb_trabajadormes',
    sa.Column('codTrabajadorMes', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('runEspecialista', mysql.VARCHAR(charset='utf8mb4', collation='utf8mb4_0900_ai_ci', length=10), nullable=False),
    sa.Column('fecha', sa.DATE(), nullable=False),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('tb_estadotrabajo',
    sa.Column('codEstadoTrabajo', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('estado', mysql.VARCHAR(length=20), nullable=False),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('tb_direccion',
    sa.Column('codDireccion', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('calle', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('nCalle', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('lat', mysql.VARCHAR(length=150), nullable=False),
    sa.Column('long', mysql.VARCHAR(length=150), nullable=False),
    sa.Column('codComuna', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('codDireccion'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('comuna_direccion', 'tb_direccion', ['codComuna'], unique=False)
    op.create_table('tb_rubro',
    sa.Column('codRubro', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('nombreRubro', mysql.VARCHAR(length=200), nullable=False),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('tb_especialista',
    sa.Column('run', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('nombres', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('apellidos', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('telefono', mysql.VARCHAR(length=9), nullable=False),
    sa.Column('correo', mysql.VARCHAR(length=60), nullable=False),
    sa.Column('contrasena', mysql.VARCHAR(length=60), nullable=False),
    sa.Column('codDireccion', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('codProfesion', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('cedulaFrontal', mysql.VARCHAR(length=2000), nullable=False),
    sa.Column('cedulaTrasera', mysql.VARCHAR(length=2000), nullable=False),
    sa.Column('certAntecedentes', mysql.VARCHAR(length=2000), nullable=False),
    sa.Column('fotoPerfil', mysql.VARCHAR(length=2000), nullable=False),
    sa.Column('tituloProfesional', mysql.VARCHAR(length=2000), nullable=False),
    sa.Column('disponibilidad', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('tb_detalleordenservicio',
    sa.Column('codDetalleOrden', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('codTrabajoEspecialista', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('codRubro', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('cantServicios', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('codDetalleOrden'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('trabajosEspecialista_detalleOrdenServicio', 'tb_detalleordenservicio', ['codTrabajoEspecialista'], unique=False)
    op.create_index('detalleOrdenServicio_rubro', 'tb_detalleordenservicio', ['codRubro'], unique=False)
    op.create_table('tb_fotostrabajos',
    sa.Column('codFotosTrabajos', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('foto1', mysql.VARCHAR(length=500), nullable=False),
    sa.Column('foto2', mysql.VARCHAR(length=500), nullable=False),
    sa.Column('foto3', mysql.VARCHAR(length=500), nullable=False),
    sa.Column('foto4', mysql.VARCHAR(length=500), nullable=False),
    sa.Column('foto5', mysql.VARCHAR(length=500), nullable=False),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    op.create_table('tb_provincia',
    sa.Column('codProvincia', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('nombreProvincia', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('codRegion', mysql.VARCHAR(length=4), nullable=False),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('tb_trabajo',
    sa.Column('codTrabajo', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('codOrdenServicio', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('codEstadoTrabajo', mysql.INTEGER(), autoincrement=False, nullable=False),
    mysql_default_charset='utf8mb3',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###