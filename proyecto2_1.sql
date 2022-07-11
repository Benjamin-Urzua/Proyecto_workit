-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-07-2022 a las 07:19:54
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `proyecto2.1`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_autentificar_cliente` (IN `_correo` VARCHAR(60), IN `_contrasena` VARCHAR(60))  BEGIN
	if((select count(*) FROM tb_cliente where  correo=_correo and contrasena=_contrasena and codEstado=1)>0)THEN
    	select 'Usuario Correcto' as msg, 1 as codigo, run from tb_cliente where correo=_correo and contrasena=_contrasena ;
    else
    	select 'Credenciales incorrectas' as msg, -1 as codigo;
    end if ;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_autentificar_especialista` (IN `_correo` VARCHAR(12), IN `_contrasena` VARCHAR(50))  BEGIN
	if((select count(*) FROM tb_especialista where  correo=_correo and contrasena=_contrasena)>0)THEN
    	select 'Usuario Correcto' as msg, 1 as codigo;
    else
    	select 'Usuario y/o password incorrecto' as msg, -1 as codigo;
    end if ;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deleteRegistroTrabajo` (IN `_codTrabajoEspecialista` INT)  BEGIN 
	if((select count(*) from tb_trabajosespecialista where codTrabajoEspecialista=_codTrabajoEspecialista)>0)THEN
    	-- Debemos saber si eliminamos o cambiamos de estado
        if((select count(*)from tb_trabajosespecialista where codTrabajoEspecialista=_codTrabajoEspecialista)>0)then
        -- Existe el trabajo... Cambiaremos de estado.. (Eliminado)
        update tb_trabajosespecialista set codEstado=3 where codTrabajoEspecialista=_codTrabajoEspecialista;
        select 'Se ha cambiado el estado del trabajo a Eliminado' as msg, 2 as codigo;
        ELSE
        -- trabajo NO está asociado, por ende lo eliminaremos...
        delete from tb_trabajosespecialista where codTrabajoEspecialista=_codTrabajoEspecialista;
        select 'Trabajo Eliminado Correctamente!' as msg, 1 as codigo;
        end if;
    ELSE
    	select 'Casi... pero NO existe codigo de trabajo asociado algún Trabajo'as msg,-1 as codigo;
    end if;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_eliminarCliente` (IN `_run` VARCHAR(13))  BEGIN 
	IF ((SELECT COUNT(*) FROM tb_cliente WHERE run = _run)>0)THEN
    
		IF ((SELECT COUNT(*) FROM tb_cliente WHERE run=_run)>0) THEN
        	UPDATE tb_cliente SET codEstado=3 WHERE run = _run;
        	SELECT 'Se ha cambiado el estado del cliente a eliminado' AS msg, 2 AS 	codigo;
        
      	ELSE
       
       		DELETE FROM tb_cliente WHERE run=_run;
       		SELECT 'El usuario Cliente a sido eliminado correctamente' AS msg, 1 as codigo;
       
       	END IF;
    
    ELSE
    
    	SELECT 'El run ingresado no coincide con nuestros registros' AS msg, -1 as codigo;
    
    END IF;
    
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_eliminarComuna` (IN `_codComuna` INT)  BEGIN 
	IF ((SELECT COUNT(*) FROM tb_comuna WHERE codComuna = _codComuna)>0)THEN
    
		IF ((SELECT COUNT(*) FROM tb_comuna WHERE codComuna = _codComuna)>0) THEN
        	UPDATE tb_comuna SET codEstado=3 WHERE codComuna = _codComuna;
        	SELECT 'Se ha cambiado el estado de la comuna a eliminada' AS msg, 2 AS 	codigo;
        
      	ELSE
       
       		DELETE FROM tb_comuna WHERE codComuna = _codComuna;
       		SELECT 'La comuna a sido eliminada correctamente' AS msg, 1 as codigo;
       
       	END IF;
    
    ELSE
    
    	SELECT 'La comuna ingresada no coincide con nuestros registros' AS msg, -1 as codigo;
    
    END IF;
    
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_eliminarDireccion` (IN `_codDireccion` INT)  BEGIN 
	IF ((SELECT COUNT(*) FROM tb_direccion WHERE codDireccion = _codDireccion)>0)THEN
    
		IF ((SELECT COUNT(*) FROM tb_direccion WHERE codDireccion =_codDireccion)>0) THEN
        	UPDATE tb_direccion SET codEstado=3 WHERE codDireccion = _codDireccion;
        	SELECT 'Se ha cambiado el estado de la dirección a eliminada' AS msg, 2 AS 	codigo;
        
      	ELSE
       
       		DELETE FROM tb_direccion WHERE codDireccion =_codDireccion;
       		SELECT 'La dirección a sido eliminada correctamente' AS msg, 1 as codigo;
       
       	END IF;
    
    ELSE
    
    	SELECT 'La dirección ingresada no coincide con nuestros registros' AS msg, -1 as codigo;
    
    END IF;
    
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_eliminarEspecialista` (IN `_run` INT)  BEGIN 
	IF ((SELECT COUNT(*) FROM tb_especialista WHERE run = _run)>0)THEN
    
		IF ((SELECT COUNT(*) FROM tb_especialista WHERE run=_run)>0) THEN
        	UPDATE tb_especialista SET codEstado=3 WHERE run = _run;
        	SELECT 'Se ha cambiado el estado del especialista a eliminado' AS msg, 2 AS 	codigo;
        
      	ELSE
       
       		DELETE FROM tb_especialista WHERE run=_run;
       		SELECT 'El usuario especialista a sido eliminado correctamente' AS msg, 1 as codigo;
       
       	END IF;
    
    ELSE
    
    	SELECT 'El run ingresado no coincide con nuestros registros' AS msg, -1 as codigo;
    
    END IF;
    
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_eliminarProfesion` (IN `_codProfesion` INT)  BEGIN 
	IF ((SELECT COUNT(*) FROM tb_profesion WHERE codProfesion = _codProfesion)>0)THEN
    
		IF ((SELECT COUNT(*) FROM tb_profesion WHERE codProfesion=_codProfesion)>0) THEN
        	UPDATE tb_profesion SET codEstado=3 WHERE codProfesion = _codProfesion;
        	SELECT 'Se ha cambiado el estado de la profesión a eliminada' AS msg, 2 AS 	codigo;
        
      	ELSE
       
       		DELETE FROM tb_profesion WHERE codProfesion = _codProfesion;
       		SELECT 'La profesión a sido eliminado correctamente' AS msg, 1 as codigo;
       
       	END IF;
    
    ELSE
    
    	SELECT 'La profesión ingresada no coincide con nuestros registros' AS msg, -1 as codigo;
    
    END IF;
    
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_eliminarProvincia` (IN `_codProvincia` INT)  BEGIN 
	IF ((SELECT COUNT(*) FROM tb_provincia WHERE codProvincia = _codProvincia)>0)THEN
    
		IF ((SELECT COUNT(*) FROM tb_provincia WHERE codProvincia=_codProvincia)>0) THEN
        	UPDATE tb_provincia SET codEstado=3 WHERE codProvincia = _codProvincia;
        	SELECT 'Se ha cambiado el estado de la provincia a eliminada' AS msg, 2 AS 	codigo;
        
      	ELSE
       
       		DELETE FROM tb_provincia WHERE codProvincia=_codProvincia;
       		SELECT 'La provincia a sido eliminada correctamente' AS msg, 1 as codigo;
       
       	END IF;
    
    ELSE
    
    	SELECT 'La provincia ingresada no coincide con nuestros registros' AS msg, -1 as codigo;
    
    END IF;
    
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_eliminarRegion` (IN `_codRegion` INT)  BEGIN 
	IF ((SELECT COUNT(*) FROM tb_region WHERE codRegion = _codRegion)>0)THEN
    
		IF ((SELECT COUNT(*) FROM tb_region WHERE codRegion = _codRegion)>0) THEN
        	UPDATE tb_region SET codEstado=3 WHERE codRegion = _codRegion;
        	SELECT 'Se ha cambiado el estado de la Región a eliminada' AS msg, 2 AS 	codigo;
        
      	ELSE
       
       		DELETE FROM tb_region WHERE codRegion = _codRegion;
       		SELECT 'La región a sido eliminada correctamente' AS msg, 1 as codigo;
       
       	END IF;
    
    ELSE
    
    	SELECT 'La región ingresada no coincide con nuestros registros' AS msg, -1 as codigo;
    
    END IF;
    
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_eliminarRubro` (IN `_codRubro` INT)  BEGIN 
	IF ((SELECT COUNT(*) FROM tb_rubro WHERE codRubro = _codRubro)>0)THEN
    
		IF ((SELECT COUNT(*) FROM tb_rubro WHERE codRubro = _codRubro)>0) THEN
        	UPDATE tb_rubro SET codEstado=3 WHERE codRubro = _codRubro;
        	SELECT 'Se ha cambiado el estado del rubro a eliminado' AS msg, 2 AS 	codigo;
        
      	ELSE
       
       		DELETE FROM tb_rubro WHERE codRubro = _codRubro;
       		SELECT 'El rubro a sido eliminado correctamente' AS msg, 1 as codigo;
       
       	END IF;
    
    ELSE
    
    	SELECT 'El rubro ingresado no coincide con nuestros registros' AS msg, -1 as codigo;
    
    END IF;
    
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_generar_detalleordenservicio` (IN `_codDetalleOrden` INT(11), IN `_codTrabajoEspecialista` INT(11), IN `_codRubro` INT(11), IN `_cantServicios` INT(11))  BEGIN  
    insert into tb_detalleordenservicio values(_codDetalleOrden,_codTrabajoEspecialista,_codRubro,_cantServicios);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_generar_direccion` (IN `_nombreRegion` VARCHAR(100), IN `_nombreProvincia` VARCHAR(100), IN `_nombreComuna` VARCHAR(100), IN `_calle` VARCHAR(100), IN `_nCalle` VARCHAR(20), IN `_lat` VARCHAR(150), IN `_lng` VARCHAR(150))  BEGIN
		-- INSERT REGION
        
    	-- Insert | Omitir
        if((select count(*) from tb_region where nombreRegion=_nombreRegion)>0)THEN
        	-- Existe... OMITIR
            select 'El registro ya existe, será omitido' as msg, 1 as codigo;
        else
        	-- No existe... INSERT
            insert into tb_region values(NULL,_nombreRegion, 1);
            select 'Registro Insertado Correctamente!' as msg, 2 as codigo;
        end if;
        
        
        -- INSERT PROVINCIA
        
        -- select codRegion
        select @codRegion := codRegion FROM tb_region WHERE nombreRegion=_nombreRegion;
        
    	-- Insert | Omitir
        if((select count(*) from tb_provincia where nombreProvincia=_nombreProvincia)>0)THEN
        	-- Existe... OMITIR
            select 'El registro ya existe, será omitido' as msg, 1 as codigo;
        else
        	-- No existe... INSERT
            insert into tb_provincia values(NULL, _nombreProvincia, @codRegion, 1);
            select 'Registro Insertado Correctamente!' as msg, 2 as codigo;
        end if;
        
        
        -- INSERT COMUNA
        
        -- select codProvincia
        select @codProvincia := codProvincia FROM tb_provincia WHERE nombreProvincia=_nombreProvincia;
        
    	-- Insert | Omitir
        if((select count(*) from tb_comuna where nombreComuna=_nombreComuna)>0)THEN
        	-- Existe... OMITIR
            select 'El registro ya existe, será omitido' as msg, 1 as codigo;
        else
        	-- No existe... INSERT
            insert into tb_comuna values(NULL,_nombreComuna, @codProvincia, 1);
            select 'Registro Insertado Correctamente!' as msg, 2 as codigo;
        end if;
        
        
        -- INSERT DIRECCION
        
        -- select codComuna
        select @codComuna := codComuna FROM tb_comuna WHERE nombreComuna=_nombreComuna;
        
    	-- Insert
        if((select count(*) from tb_direccion where lat=_lat and lng=_lng)>0)THEN
        	-- Existe... OMITIR
            select 'El registro ya existe, será omitido' as msg, 1 as codigo;
        else
        	-- No existe... INSERT
            insert into tb_direccion values(NULL, _calle, _nCalle, _lat, _lng, @codComuna, 1);
            select 'Registro Insertado Correctamente!' as msg, 2 as codigo;
        end if;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_generar_ordenservicio` (IN `_codOrdenServicio` INT(11), IN `_nombreServicio` VARCHAR(60), IN `_runCliente` VARCHAR(10), IN `_runEspecialista` VARCHAR(10), IN `_fechaInicio` DATE, IN `_fechaFin` DATE, IN `_codDireccion` INT(11), IN `_descripción` VARCHAR(500), IN `_codDetalleOrden` INT(11), IN `_codTrabajoEspecialista` INT(11), IN `_codRubro` INT(11), IN `_cantServicios` INT(11))  BEGIN
	call sp_generar_detalleordenservicio((SELECT MAX(codDetalleOrden) + 1 FROM tb_detalleordenservicio),_codTrabajoEspecialista, _codRubro, _cantServicios);

    insert into tb_ordenservicio values(_codOrdenServicio,_nombreServicio,_runCliente,_runEspecialista, _fechaInicio, _fechaFin, _codDireccion, _descripción, (select MAX(codDetalleOrden) + 1 FROM tb_detalleordenservicio));
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_generar_preguntaRespuesta` (IN `_codPregunta` INT, IN `_respuesta` VARCHAR(200))  BEGIN
	insert into tb_respuestaseguridad values(NULL,_respuesta);
    
    select @codRespuesta := codRespuesta FROM tb_respuestaseguridad WHERE respuesta=_respuesta;
    
    insert into tb_preguntarespuesta values(NULL,_codPregunta, @codRespuesta);
   	select 'Registro insertado correctamente' as msg, 2 as codigo;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insModPreguntasSeguridad` (IN `_codPregunta` INT, IN `_pregunta` VARCHAR(200))  BEGIN 
	IF((SELECT COUNT(*) FROM tb_preguntasseguridad WHERE codPregunta = _codPregunta)>0) THEN
       
       UPDATE tb_preguntasseguridad SET pregunta = _pregunta WHERE codPregunta = _codPregunta;
       SELECT 'Registro Actualizado' as msg, 2 as codigo;
    ELSE
    	
        INSERT INTO tb_preguntasseguridad VALUES (_codPregunta, _pregunta);
        SELECT 'Registro insertado correctamente' as msg, 1 as codigo;

    END IF ;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insModProfesion` (IN `_codProfesion` INT, IN `_nombreProfesion` VARCHAR(100), IN `_codRubro` INT, IN `_codEstado` INT)  BEGIN 
	IF((SELECT COUNT(*) FROM tb_profesion WHERE codProfesion = _codProfesion)>0) THEN
       
       UPDATE tb_profesion SET nombreProfesion = _nombreProfesion, codRubro = _codRubro, codEstado = _codEstado WHERE codProfesion = _codProfesion;
       SELECT 'Registro Actualizado' as msg, 2 as codigo;
    ELSE
    	
        INSERT INTO tb_profesion VALUES (_codProfesion, _nombreProfesion, _codRubro, _codEstado);
        SELECT 'Registro insertado correctamente' as msg, 1 as codigo;
        
        END if;
        END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insModTrabajadorMes` (IN `_codTrabajadorMes` INT, IN `_runEspecialista` VARCHAR(10), IN `_fecha` DATE)  BEGIN 
	IF((SELECT COUNT(*) FROM tb_trabajadormes WHERE codTrabajadorMes = _codTrabajadorMes)>0) THEN
       
       UPDATE tb_trabajadormes SET runEspecialista = _runEspecialista, fecha = _fecha WHERE codTrabajadorMes = _codTrabajadorMes;
       SELECT 'Registro Actualizado' as msg, 2 as codigo;
    ELSE
    	
        INSERT INTO tb_trabajadormes VALUES (_codTrabajadorMes, _runEspecialista, _fecha);
        SELECT 'Registro insertado correctamente' as msg, 1 as codigo;

    END IF ;
    END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insMod_cliente` (IN `_run` VARCHAR(10), IN `_nombres` VARCHAR(100), IN `_apellidos` VARCHAR(100), IN `_telefono` INT(9), IN `_correo` VARCHAR(60), IN `_contrasena` VARCHAR(60), IN `_codDireccion` INT, IN `_codRespuesta` INT, IN `_fechaNacto` DATE, IN `_codPerfilCli` INT(11), IN `_codEstado` INT)  BEGIN 
	IF((SELECT COUNT(*) FROM tb_cliente WHERE run = _run)>0) THEN
       
       UPDATE tb_cliente SET run = _run, nombres = _nombres, apellidos = _apellidos, telefono = _telefono, correo = _correo, contrasena = _contrasena, codDireccion = _codDireccion, codRespuesta = _codRespuesta, fechaNacto = _fechaNacto, codPerfilCli = _codPerfilCli, codEstado = _codEstado;
       SELECT 'Registro Actualizado' as msg, 2 as codigo;
    ELSE
    	
        INSERT INTO tb_cliente VALUES (_run,_nombres, _apellidos, _telefono, _correo, _contrasena, _codDireccion, _codRespuesta, _fechaNacto, _codPerfilCli, _codEstado);
        call sp_insMod_perfilCliente(_codPerfilCli, '', '');
        SELECT 'Registro insertado correctamente' as msg, 1 as codigo;

    END IF ;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insMod_detalleordenservicio` (IN `_codDetalleOrden` INT, IN `_codTrabajoEspecialista` INT, IN `_codRubro` INT, IN `_cantServicios` INT)  BEGIN 
	IF((SELECT COUNT(*) FROM tb_detalleservicio WHERE codDetalleOrden = _codDetalleOrden)>0) THEN
       
       UPDATE tb_detalleordenservicio SET codTrabajoEspecialista = _codTrabajoEspecialista, codRubro = _codRubro, cantServicios = _cantServicios WHERE codDetalleOrden = _codDetalleOrden;
       SELECT 'Registro Actualizado' as msg, 2 as codigo;
    ELSE
    	
        INSERT INTO tb_detalleordenservicio VALUES (_codDetalleOrden, _codTrabajoEspecialista, _codRubro, _cantServicios);
        SELECT 'Registro insertado correctamente' as msg, 1 as codigo;

    END IF ;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insMod_direccion` (IN `_calle` VARCHAR(100), IN `_nCalle` VARCHAR(20), IN `_lat` VARCHAR(150), IN `_lng` VARCHAR(150), IN `_codComuna` INT, IN `_codEstado` INT)  BEGIN
        INSERT INTO tb_direccion VALUES (NULL, _calle, _nCalle, _lat, _lng, _codComuna, _codEstado);
        SELECT 'Registro insertado correctamente' as msg, 1 as codigo;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insMod_especialista` (IN `_run` VARCHAR(10), IN `_nombres` VARCHAR(100), IN `_apellidos` VARCHAR(100), IN `_telefono` VARCHAR(9), IN `_correo` VARCHAR(60), IN `_contrasena` VARCHAR(60), IN `_codProfesion` INT, IN `_codDireccion` INT, IN `_cedulaFrontal` VARCHAR(2000), IN `_cedulaTrasera` VARCHAR(2000), IN `_certAntecedentes` VARCHAR(2000), IN `_fotoPerfil` VARCHAR(2000), IN `_tituloProfesional` VARCHAR(2000), IN `_disponibilidad` INT, IN `_codEstado` INT)  BEGIN 
	IF((SELECT COUNT(*) FROM tb_especialista WHERE run = _run)>0) THEN
       
       UPDATE tb_especialista SET run = _run, nombres = _nombres, apellidos = _apellidos, telefono = _telefono, correo = _correo, contrasena = _contrasena, codProfesion = _codProfesion, codDireccion = _codDireccion, cedulaFrontal = _cedulaFrontal, cedulaTrasera = _cedulaTrasera, certAntecedentes = _certAntecedentes, fotoPerfil = _fotoPerfil, tituloProfesional = _tituloProfesional, disponibilidad = _disponibilidad, codEstado = _codEstado;
       SELECT 'Registro Actualizado' as msg, 2 as codigo;
    ELSE
    	
        INSERT INTO tb_especialista VALUES (_run,_nombres, _apellidos, _telefono, _correo, _contrasena, _codProfesion, _codDireccion, _cedulaFrontal, _cedulaTrasera, _certAntecedentes, _fotoPerfil, _tituloProfesional, _disponibilidad, _codEstado);
        SELECT 'Registro insertado correctamente' as msg, 1 as codigo;

    END IF ;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insMod_estadoTrabajo` (IN `_codEstadoTrabajo` INT, IN `_estado` VARCHAR(20))  BEGIN 
	IF((SELECT COUNT(*) FROM tb_estadotrabajo WHERE codEstadoTrabajo = _codEstadoTrabajo)>0) THEN
       
       UPDATE tb_estadotrabajo SET estado = _estado WHERE codEstadoTrabajo = _codEstadoTrabajo;
       SELECT 'Registro Actualizado' as msg, 2 as codigo;
    ELSE
    	
        INSERT INTO tb_estadotrabajo VALUES (_codEstadoTrabajo, _estado);
        SELECT 'Registro insertado correctamente' as msg, 1 as codigo;

    END IF;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insMod_fotosTrabajos` (IN `_codFotosTrabajos` INT, IN `_foto1` VARCHAR(500), IN `_foto2` VARCHAR(500), IN `_foto3` VARCHAR(500), IN `_foto4` VARCHAR(500), IN `_foto5` VARCHAR(500))  BEGIN 
	IF((SELECT COUNT(*) FROM tb_fotostrabajos WHERE codFotosTrabajos = _codFotosTrabajos)>0) THEN
       
       UPDATE tb_fotostrabajos SET  foto1 = _foto1, foto2 = _foto2, foto3 = _foto3, foto4 = _foto4, foto5 = _foto5 WHERE codFotosTrabajos = _codFotosTrabajos;
       SELECT 'Registro Actualizado' as msg, 2 as codigo;
    ELSE
    	
        INSERT INTO tb_fotostrabajos VALUES (_codFotosTrabajos,_foto1, _foto2, _foto3, _foto4, _foto5);
        SELECT 'Registro insertado correctamente' as msg, 1 as codigo;

    END IF ;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insMod_ordenServicio` (IN `_codOrdenServicio` INT, IN `_nombreServicio` VARCHAR(60), IN `_runCliente` VARCHAR(10), IN `_runEspecialista` VARCHAR(10), IN `_fechaInicio` DATE, IN `_fechaFin` DATE, IN `_codDireccion` INT, IN `_descripcion` VARCHAR(500), IN `_codDetalleOrden` INT, IN `_codEstado` INT)  BEGIN 
	IF((SELECT COUNT(*) FROM tb_ordenservicio WHERE codOrdenServicio = _codOrdenServicio)>0) THEN
       
       UPDATE tb_ordenservicio SET  nombreServicio = _nombreServicio, runCliente = _runCliente, runEspecialista = _runEspecialista, fechaInicio = _fechaInicio, fechaFin = _fechaFin, codDireccion = _codDireccion , descripcion = _descripcion, codDetalleOrden = _codDetalleOrden, codEstado = _codEstado WHERE codOrdenServicio = _codOrdenServicio;
       SELECT 'Registro Actualizado' as msg, 2 as codigo;
    ELSE
    	
        INSERT INTO tb_ordenservicio VALUES (_codOrdenServicio, _nombreServicio, _runCliente, _runEspecialista, _fechaInicio, _fechaFin, _codDireccion, _descripcion, _codDetalleOrden, _codEstado);
        SELECT 'Registro insertado correctamente' as msg, 1 as codigo;

    END IF ;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insMod_perfilEspecialista` (IN `_codPerfilEsp` INT, IN `_codTrabajoEspecialista` INT, IN `_descripcionPersonal` VARCHAR(500), IN `_descripcionServicios` VARCHAR(5000))  BEGIN 
	IF((SELECT COUNT(*) FROM tb_especialista WHERE codPerfilEsp = _codPerfilEsp)>0) THEN
       
       UPDATE tb_perfilespecialista SET  codTrabajoEspecialista = _codTrabajoEspecialista, descripcionPersonal = _descripcionPersonal, descripcionServicios = _descripcionServicios WHERE codPerfilEsp = _codPerfilEsp;
       SELECT 'Registro Actualizado' as msg, 2 as codigo;
    ELSE
    	
        INSERT INTO tb_perfilespecialista VALUES (_codPerfilEsp, _codTrabajoEspecialista, _descripcionPersonal, _descripcionServicios);
        SELECT 'Registro insertado correctamente' as msg, 1 as codigo;

    END IF ;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insMod_reporte` (IN `_codReporte` INT, IN `_runEspecialista` VARCHAR(10), IN `_runCliente` VARCHAR(10), IN `_motivo` VARCHAR(300), IN `_prueba` VARCHAR(500))  BEGIN 
	IF((SELECT COUNT(*) FROM tb_reporte WHERE codReporte = _codReporte)>0) THEN
       
       UPDATE tb_reporte SET runEspecialista = _runEspecialista, runCliente = _runCliente, motivo = _motivo, prueba = _prueba WHERE codReporte = _codReporte;
       SELECT 'Registro Actualizado' as msg, 2 as codigo;
    ELSE
    	
        INSERT INTO tb_reporte VALUES (_codReporte, _runEspecialista, _runCliente, _motivo, _prueba);
        SELECT 'Registro insertado correctamente' as msg, 1 as codigo;

    END IF ;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insMod_resena` (IN `_codResena` INT, IN `_runCliente` VARCHAR(10), IN `_runEspecialista` VARCHAR(10), IN `_resena` VARCHAR(1000), IN `_calificacion` INT)  BEGIN 
	IF((SELECT COUNT(*) FROM tb_resena WHERE codResena = _codResena)>0) THEN
       
       UPDATE tb_resena SET runCliente= _runCliente, runEspecialista = _runEspecialista, resena =_resena, calificacion =_calificacion WHERE codResena = _codResena;
       SELECT 'Registro Actualizado' as msg, 2 as codigo;
    ELSE
    	
        INSERT INTO tb_resena VALUES (_codResena, _runCliente, _runEspecialista, _resena, _calificacion);
        SELECT 'Registro insertado correctamente' as msg, 1 as codigo;

    END IF ;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insMod_respuestaSeguridad` (IN `_codRespuesta` INT, IN `_codPregunta` INT, IN `_respuesta` VARCHAR(200))  BEGIN 
	IF((SELECT COUNT(*) FROM tb_respuestaseguridad WHERE codRespuesta = _codRespuesta)>0) THEN
       
       UPDATE tb_respuestaseguridad SET codPregunta = _codPregunta, respuesta = _respuesta WHERE codRespuesta = _codRespuesta;
       SELECT 'Registro Actualizado' as msg, 2 as codigo;
    ELSE
    	
        INSERT INTO tb_respuestaseguridad VALUES (_codRespuesta, _codPregunta,_respuesta);
        SELECT 'Registro insertado correctamente' as msg, 1 as codigo;

    END IF ;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insMod_rubro` (IN `_codRubro` INT, IN `_nombreRubro` VARCHAR(200), IN `_codEstado` INT)  BEGIN 
	IF((SELECT COUNT(*) FROM tb_rubro WHERE codRubro = _codRubro)>0) THEN
       
       UPDATE tb_rubro SET nombreRubro = _nombreRubro, codEstado = _codEstado WHERE codRubro = _codRubro;
       SELECT 'Registro Actualizado' as msg, 2 as codigo;
    ELSE
    	
        INSERT INTO tb_rubro VALUES (_codRubro, _nombreRubro, _codEstado);
        SELECT 'Registro insertado correctamente' as msg, 1 as codigo;
END IF;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insMod_trabajo` (IN `_codTrabajo` INT, IN `_codOrdenServicio` INT, IN `_codEstadoTrabajo` INT)  BEGIN 
	IF((SELECT COUNT(*) FROM tb_trabajo WHERE codTrabajo = _codTrabajo)>0) THEN
       
       UPDATE tb_trabajo SET codOrdenServicio = _codOrdenServicio, codEstadoTrabajo = _codEstadoTrabajo WHERE codTrabajo = _codTrabajo;
       SELECT 'Registro Actualizado' as msg, 2 as codigo;
    ELSE
    	
        INSERT INTO tb_trabajo VALUES (_codTrabajo, _codOrdenServicio, _codEstadoTrabajo);
        SELECT 'Registro insertado correctamente' as msg, 1 as codigo;

    END IF;
    END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_insMod_trabajosEspecialista` (IN `_codTrabajoEspecialista` INT, IN `_nombreTrabajo` VARCHAR(100), IN `_valorTrabajo` INT, IN `_descripcionTrabajo` VARCHAR(400), IN `_codFotosTrabajos` INT, IN `_codEstado` INT)  BEGIN 
	IF((SELECT COUNT(*) FROM tb_trabajosespecialista WHERE codTrabajoEspecialista = _codTrabajoEspecialista)>0) THEN
       
       UPDATE tb_trabajosespecialista SET nombreTrabajo = _nombreTrabajo, valorTrabajo = _valorTrabajo, descripcionTrabajo = _descripcionTrabajo , codFotosTrabajos = _codFotosTrabajos, codEstado = _codEstado WHERE codTrabajoEspecialista = _codTrabajoEspecialista;
       SELECT 'Registro Actualizado' as msg, 2 as codigo;
    ELSE
    	
        INSERT INTO tb_trabajosespecialista VALUES (_codTrabajoEspecialista, _nombreTrabajo, _valorTrabajo, _descripcionTrabajo, _codFotosTrabajos, _codEstado);
        SELECT 'Registro insertado correctamente' as msg, 1 as codigo;

    END IF;
    END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_ins_cliente` (IN `_run` VARCHAR(12), IN `_nombres` VARCHAR(100), IN `_apellidos` VARCHAR(100), IN `_telefono` VARCHAR(9), IN `_correo` VARCHAR(60), IN `_contrasena` VARCHAR(60), IN `_fechaNacto` DATE)  BEGIN
        -- select codDireccion
        select @codDireccion := max(codDireccion) FROM tb_direccion;
        
        -- select codPreguntaRespuesta
        select @codPreguntaRespuesta := max(codPreguntaRespuesta) FROM tb_preguntarespuesta;
        
        -- select codPerfilCli
        select @codPerfilCli := max(codPerfilCli) FROM tb_perfilcliente;
        
        -- NO EXISTE... INSERT
        insert ignore into tb_cliente values(_run,_nombres,_apellidos,_telefono,_correo,_contrasena, @codDireccion, @codPreguntaRespuesta, _fechaNacto, @codPerfilCli, 1);
        select 'Registro Insertado Correctamente!' as msg, 1 as codigo;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_ins_comuna` (IN `_nombreComuna` VARCHAR(12), IN `_codProvincia` INT, IN `_codEstado` INT)  BEGIN
	-- INSERT COMUNA
        
    	-- Insert | Omitir
        if((select count(*) from tb_comuna where nombreComuna=_nombreComuna)>0)THEN
        	-- Existe... OMITIR
            select 'El registro ya existe, será omitido' as msg, -1 as codigo;
        else
        	-- No existe... INSERT
            insert into tb_comuna values(NULL, _nombreComuna, _codProvincia, _codEstado);
            select 'Registro Insertado Correctamente!' as msg, 1 as codigo;
        end if;
        
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_ins_perfilcliente` (IN `_descripcion` VARCHAR(500), IN `_fotoPerfil` VARCHAR(2000))  BEGIN
        INSERT INTO tb_perfilcliente VALUES(NULL, _descripcion, _fotoPerfil) ;
        SELECT 'Registro insertado correctamente' AS msg, 1 AS codigo ;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_ins_provincia` (IN `_nombreProvincia` VARCHAR(100), IN `_codRegion` INT, IN `_codEstado` INT)  BEGIN
		-- INSERT PROVINCIA

    	-- Insert | Omitir
        if((select count(*) from tb_provincia where nombreProvincia=_nombreProvincia)>0)THEN
        	-- Existe... OMITIR
            select 'El registro ya existe, será omitido' as msg, -1 as codigo;
        else
        	-- No existe... INSERT
            insert into tb_provincia values(NULL, _nombreProvincia, _codRegion, _codEstado);
            select 'Registro Insertado Correctamente!' as msg, 1 as codigo;
        end if;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_ins_region` (IN `_nombreRegion` VARCHAR(100), IN `_codEstado` INT)  BEGIN
		-- INSERT REGION
        insert into tb_region values(NULL,_nombreRegion, _codEstado);
            select 'Registro Insertado Correctamente!' as msg, 1 as codigo;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_retornar_historial` (IN `_runCliente` VARCHAR(13))  BEGIN
	if((select count(*) from tb_trabajo trab
    join tb_ordenservicio ord 
    on trab.codOrdenServicio=ord.codOrdenServicio
    where ord.runCliente = _runCliente)>0)THEN
    
    select * from vw_historial_clientes
    where run = _runCliente;
    else
    	select 'Historial vacio' as msg, -1 as codigo;
    end if ;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_retornar_perfilCliente` (IN `_run` VARCHAR(13))  BEGIN
	select perf.*, cli.nombres, cli.apellidos from tb_cliente cli inner join tb_perfilcliente as perf on perf.codPerfilCli = cli.codPerfilCli where cli.run = _run;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_update_perfilCliente` (IN `_run` VARCHAR(13), IN `_descripcion` VARCHAR(500), IN `_fotoPerfil` VARCHAR(2000))  BEGIN	
	select @codPerfilCli:= codPerfilCli from tb_cliente where run = _run;  	
    UPDATE tb_perfilcliente SET descripcion = _descripcion, fotoPerfil = _fotoPerfil where codPerfilCli = @codPerfilCli    ;
	SELECT 'Perfil actualizado correctamente' AS msg, 1 AS codigo ;
    
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_cliente`
--

CREATE TABLE `tb_cliente` (
  `run` varchar(13) NOT NULL,
  `nombres` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `telefono` int(9) NOT NULL,
  `correo` varchar(60) NOT NULL,
  `contrasena` varchar(60) NOT NULL,
  `codDireccion` int(11) NOT NULL,
  `codPreguntaRespuesta` int(11) NOT NULL,
  `fechaNacto` date NOT NULL,
  `codPerfilCli` int(11) NOT NULL,
  `codEstado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tb_cliente`
--

INSERT INTO `tb_cliente` (`run`, `nombres`, `apellidos`, `telefono`, `correo`, `contrasena`, `codDireccion`, `codPreguntaRespuesta`, `fechaNacto`, `codPerfilCli`, `codEstado`) VALUES
('1.506.777-2', 'Gerardo Gerardo', 'Benitez Daza', 123456789, 'gerar@gmail.com', 'contrasena1', 43, 45, '2022-07-01', 46, 1),
('1.574.457-k', 'Felipe Juan', 'Cerros Castillo', 123456789, 'felipe@gmail.com', 'contrasena1', 35, 36, '2022-05-04', 37, 3),
('10.118.434-k', 'Luis Eduardo', 'Ortiz Morales', 12345678, 'luis@gmail.com', 'contrasena1', 41, 43, '2017-02-23', 44, 1),
('13.617.957-8', 'Eduardo Gaspar', 'Morales Lopez', 12345678, 'eduga@gmail.com', 'contrasena1', 40, 42, '2022-07-09', 43, 3),
('16.405.341-5', 'Esteban Benedicto', 'Chavez Diaz', 123456789, 'est.ben@gmail.com', 'contrasena1', 36, 38, '2022-06-02', 39, 1),
('17.477.825-6', 'Estela Belen', 'Venegas ', 12345678, 'este@gmail.com', 'contrasena1', 44, 49, '2022-07-04', 50, 1),
('29.076.188-3', 'Esteban Manuel', 'Rivas Diaz', 123456789, 'esteban.man@gmail.com', 'contrasena1', 37, 39, '2022-06-06', 40, 1),
('32.492.872-3', 'Loreto Camila', 'Diaz Villareal', 12345678, 'lore@gmail.com', 'contrasena1', 42, 44, '2022-07-04', 45, 1),
('66.033.213-8', 'aaaaaa', 'aaaaaa', 123456789, 'a@a.com', '12345678', 38, 40, '2022-06-01', 41, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_comuna`
--

CREATE TABLE `tb_comuna` (
  `codComuna` int(11) NOT NULL,
  `nombreComuna` varchar(100) NOT NULL,
  `codProvincia` int(11) NOT NULL,
  `codEstado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tb_comuna`
--

INSERT INTO `tb_comuna` (`codComuna`, `nombreComuna`, `codProvincia`, `codEstado`) VALUES
(7, 'Cauquenes', 7, 1),
(15, 'Los Vilos', 0, 1),
(19, 'Alto Hospici', 0, 1),
(25, 'O’Higgins', 25, 1),
(26, 'Los Ángeles', 26, 1),
(27, 'Los+Ángeles', 26, 1),
(28, '08301', 27, 1),
(29, '10202', 28, 1),
(30, '15202', 29, 1),
(31, '04304', 30, 1),
(32, '02104', 31, 1),
(33, '03202', 32, 1),
(34, '09202', 33, 1),
(35, '07201', 34, 1),
(36, '15101', 35, 1),
(37, '11302', 36, 1),
(38, '02102', 31, 1),
(39, '01107', 37, 1),
(40, '03101', 38, 1),
(41, '04201', 39, 1),
(42, '06112', 40, 1),
(43, '05704', 41, 1),
(44, '06202', 42, 1),
(45, 'Camiña', 43, 1),
(46, 'Calama', 44, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_detalleordenservicio`
--

CREATE TABLE `tb_detalleordenservicio` (
  `codDetalleOrden` int(11) NOT NULL,
  `codTrabajoEspecialista` int(11) NOT NULL,
  `codRubro` int(11) NOT NULL,
  `cantServicios` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tb_detalleordenservicio`
--

INSERT INTO `tb_detalleordenservicio` (`codDetalleOrden`, `codTrabajoEspecialista`, `codRubro`, `cantServicios`) VALUES
(1, 1, 1, 1),
(2, 2, 1, 1),
(3, 3, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_direccion`
--

CREATE TABLE `tb_direccion` (
  `codDireccion` int(11) NOT NULL,
  `calle` varchar(100) NOT NULL,
  `nCalle` varchar(20) NOT NULL,
  `lat` varchar(150) DEFAULT NULL,
  `lng` varchar(150) DEFAULT NULL,
  `codComuna` int(11) NOT NULL,
  `codEstado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tb_direccion`
--

INSERT INTO `tb_direccion` (`codDireccion`, `calle`, `nCalle`, `lat`, `lng`, `codComuna`, `codEstado`) VALUES
(1, 'Nueva Esperanza', '1260', '-37.497067', '-72.330022', 1, 1),
(2, 'Lago Villarrica', '717', '-37.4662176', '-72.3792155,17', 1, 1),
(3, 'Los gladiolos', '999', '-9999', '9999', 2, 1),
(4, 'Los petalos azules', '1228', '-585585', '516516', 3, 1),
(5, 'Manuel Rodriguez', '1111', '-8784915', '14651919', 4, 1),
(6, 'Callelol', '222', '1', '1', 7, 1),
(13, 'CalleTest', '321', '12', '13', 15, 1),
(18, 'CalleTest', '663', '-48.46614959999999', '-72.5592154', 25, 1),
(19, 'CalleTest', '663', '-48.46614959999999', '-72.5592154', 25, 1),
(20, 'CalleTest', '663', '-48.46614959999999', '-72.5592154', 25, 1),
(21, 'CalleTest', '663', '-48.46614959999999', '-72.5592154', 25, 1),
(22, 'CalleTest', '663', '-48.46614959999999', '-72.5592154', 25, 1),
(23, 'CalleTest', '663', '-48.46614959999999', '-72.5592154', 25, 1),
(24, 'Nueva+Esperanza', '1260', '-37.4975572', '-72.3327015', 26, 1),
(25, 'Nueva+Esperanza', '1260', '-37.4975572', '-72.3327015', 26, 1),
(26, 'Nueva+Esperanza', '1260', '-37.4975572', '-72.3327015', 27, 1),
(27, 'Nueva+Esperanza', '1260', '-37.4975572', '-72.3327015', 28, 1),
(28, 'Nueva Esperanza', '1260', '-37.4975572', '-72.3327015', 28, 1),
(29, 'Las Violetas', '487', '-41.861141', '-73.8109699', 29, 1),
(30, 'Los Gladiolos', '717', '-17.8232348', '-69.58776730000001', 30, 1),
(31, 'Los Vilos', '932', '-31.9121865', '-71.5112017', 31, 1),
(32, 'La Sierra', '631', '-23.6244196', '-70.3865926', 32, 1),
(33, 'Manuel Rodriguez', '313', '-26.3882321', '-70.0468764', 33, 1),
(34, 'Los Vilos', '887', '-37.9582687', '-72.4321187', 34, 1),
(35, 'Colo Colo', '913', '-35.9676285', '-72.32223309999999', 35, 1),
(36, 'Calle España', '111', '-18.4582121', '-70.30039', 36, 1),
(37, 'Rio Oro', '441', '-23.6252499', '-70.3913681', 38, 1),
(38, 'a', '181', '-20.2686722', '-70.10491689999999', 39, 1),
(39, 'Bogota', '444', '-27.3665763', '-70.3321587', 40, 1),
(40, 'Magdalenas', '541', '-31.6308', '-71.1653', 41, 1),
(41, 'Calle Arica', '131', '-34.3921609', '-71.1667306', 42, 1),
(42, 'Los vilos', '17', '-33.0691943', '-71.5836918', 43, 1),
(43, 'Calle Lima', '213', '-34.2051972', '-71.6547276', 44, 1),
(44, 'Av Camiña', '789', '-20.2028799', '-69.2877535', 45, 1),
(45, 'Sterling Oval', '451', '-22.4543923', '-68.9293819', 46, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_especialista`
--

CREATE TABLE `tb_especialista` (
  `run` varchar(10) NOT NULL,
  `nombres` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `telefono` varchar(9) NOT NULL,
  `correo` varchar(60) NOT NULL,
  `contrasena` varchar(60) NOT NULL,
  `codDireccion` int(11) NOT NULL,
  `codProfesion` int(11) NOT NULL,
  `cedulaFrontal` varchar(2000) NOT NULL,
  `cedulaTrasera` varchar(2000) NOT NULL,
  `certAntecedentes` varchar(2000) NOT NULL,
  `codPerfilEsp` int(11) NOT NULL,
  `tituloProfesional` varchar(2000) NOT NULL,
  `disponibilidad` tinyint(1) NOT NULL,
  `codEstado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tb_especialista`
--

INSERT INTO `tb_especialista` (`run`, `nombres`, `apellidos`, `telefono`, `correo`, `contrasena`, `codDireccion`, `codProfesion`, `cedulaFrontal`, `cedulaTrasera`, `certAntecedentes`, `codPerfilEsp`, `tituloProfesional`, `disponibilidad`, `codEstado`) VALUES
('12345678-9', 'Juan', 'Perez', '987654321', 'juan@juan.cl', '12345', 2, 1, 'asdadasdad', 'asdsadasdsa', 'sadasdadas', 1, 'asdasdasd', 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_estado`
--

CREATE TABLE `tb_estado` (
  `codEstado` int(11) NOT NULL,
  `estado` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tb_estado`
--

INSERT INTO `tb_estado` (`codEstado`, `estado`) VALUES
(1, 'Habilitado'),
(2, 'Inhabilitado'),
(3, 'Eliminado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_estadotrabajo`
--

CREATE TABLE `tb_estadotrabajo` (
  `codEstadoTrabajo` int(11) NOT NULL,
  `estado` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `tb_estadotrabajo`
--

INSERT INTO `tb_estadotrabajo` (`codEstadoTrabajo`, `estado`) VALUES
(1, 'Activo'),
(2, 'Terminado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_fotostrabajos`
--

CREATE TABLE `tb_fotostrabajos` (
  `codFotosTrabajos` int(11) NOT NULL,
  `foto1` varchar(500) NOT NULL,
  `foto2` varchar(500) NOT NULL,
  `foto3` varchar(500) NOT NULL,
  `foto4` varchar(500) NOT NULL,
  `foto5` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `tb_fotostrabajos`
--

INSERT INTO `tb_fotostrabajos` (`codFotosTrabajos`, `foto1`, `foto2`, `foto3`, `foto4`, `foto5`) VALUES
(1, 'https://www.poloservices.net/wp-content/uploads/2019/04/servicio-tecnico.jpg', 'https://www.hsi.es/wp-content/uploads/2019/11/396144-PCIMTM-93-1080x675.jpg', 'https://www.banhaia.com/images/home-tab-content/tab-servicio-tecnico.jpg', 'https://noticiasrtv.com/wp-content/uploads/2019/11/1573623203_614_Como-ensamblar-tu-PC-10-consejos-a-seguir.jpg', 'https://noticiasrtv.com/wp-content/uploads/2019/11/1573623203_614_Como-ensamblar-tu-PC-10-consejos-a-seguir.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_ordenservicio`
--

CREATE TABLE `tb_ordenservicio` (
  `codOrdenServicio` int(11) NOT NULL,
  `nombreServicio` varchar(60) NOT NULL,
  `runCliente` varchar(13) NOT NULL,
  `runEspecialista` varchar(13) NOT NULL,
  `fechaInicio` date NOT NULL,
  `fechaFin` date NOT NULL,
  `codDireccion` int(11) NOT NULL,
  `descripcion` varchar(500) NOT NULL,
  `codDetalleOrden` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tb_ordenservicio`
--

INSERT INTO `tb_ordenservicio` (`codOrdenServicio`, `nombreServicio`, `runCliente`, `runEspecialista`, `fechaInicio`, `fechaFin`, `codDireccion`, `descripcion`, `codDetalleOrden`) VALUES
(4, 'Ensamblado pc Gamer', '1.506.777-2', '12345678-9', '2022-06-01', '2022-07-11', 43, 'Nueva orden', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_perfilcliente`
--

CREATE TABLE `tb_perfilcliente` (
  `codPerfilCli` int(11) NOT NULL,
  `descripcion` varchar(500) NOT NULL,
  `fotoPerfil` varchar(2000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tb_perfilcliente`
--

INSERT INTO `tb_perfilcliente` (`codPerfilCli`, `descripcion`, `fotoPerfil`) VALUES
(1, '', ''),
(2, 'A mi me gusta hacer otras cosas', 'foto'),
(3, 'Vivo en mi casa', 'foto'),
(4, 'Yo no', 'foto'),
(5, 'Tengo dos hijos', 'foto'),
(6, 'Yo tengo gatos', 'foto'),
(7, '', ''),
(8, '', ''),
(9, '', ''),
(10, '', ''),
(11, '', ''),
(12, '', ''),
(13, '', ''),
(14, '', ''),
(15, '', ''),
(16, '', ''),
(17, '', ''),
(18, '', ''),
(19, '', ''),
(20, '', ''),
(21, '', ''),
(22, '', ''),
(23, '', ''),
(24, '', ''),
(25, '', ''),
(26, '', ''),
(27, '', ''),
(28, '', ''),
(29, '', ''),
(30, '', ''),
(31, '', ''),
(32, '', ''),
(33, '', ''),
(34, '', ''),
(35, '', ''),
(36, '', ''),
(37, 'Nueva descripcion', 'blob:http://127.0.0.1:5000/05459faa-f137-46c1-a178-bad73476e30e'),
(38, '', ''),
(39, '', ''),
(40, '', ''),
(41, '', ''),
(42, '', ''),
(43, '', ''),
(44, 'Otra nueva descripcion', 'blob:http://127.0.0.1:5000/1aa03fbd-85ef-486c-a8b2-63dbbb5df632'),
(45, '', ''),
(46, '', ''),
(47, '', ''),
(48, '', ''),
(49, '', ''),
(50, '', ''),
(51, '', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_perfilespecialista`
--

CREATE TABLE `tb_perfilespecialista` (
  `codPerfilEsp` int(11) NOT NULL,
  `codTrabajoEspecialista` int(11) NOT NULL,
  `descripcionPersonal` varchar(500) NOT NULL,
  `descripcionServicios` varchar(5000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tb_perfilespecialista`
--

INSERT INTO `tb_perfilespecialista` (`codPerfilEsp`, `codTrabajoEspecialista`, `descripcionPersonal`, `descripcionServicios`) VALUES
(1, 1, 'Armo equipos de todo tipo', 'Armo equipos gamer');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_preguntarespuesta`
--

CREATE TABLE `tb_preguntarespuesta` (
  `codPreguntaRespuesta` int(11) NOT NULL,
  `codPregunta` int(11) NOT NULL,
  `codRespuesta` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tb_preguntarespuesta`
--

INSERT INTO `tb_preguntarespuesta` (`codPreguntaRespuesta`, `codPregunta`, `codRespuesta`) VALUES
(4, 4, 14),
(5, 4, 15),
(6, 4, 16),
(7, 4, 17),
(8, 4, 18),
(9, 4, 19),
(10, 4, 20),
(11, 4, 21),
(12, 4, 22),
(13, 4, 23),
(14, 4, 24),
(15, 2, 25),
(16, 2, 26),
(17, 2, 27),
(18, 3, 28),
(19, 3, 29),
(20, 3, 30),
(21, 3, 31),
(22, 1, 32),
(23, 1, 33),
(24, 1, 34),
(25, 1, 35),
(26, 1, 36),
(27, 1, 37),
(28, 1, 38),
(29, 1, 39),
(30, 1, 40),
(31, 5, 41),
(32, 5, 42),
(33, 5, 43),
(34, 5, 44),
(35, 5, 45),
(36, 2, 46),
(37, 2, 47),
(38, 4, 48),
(39, 5, 49),
(40, 2, 50),
(41, 2, 51),
(42, 3, 52),
(43, 2, 53),
(44, 2, 54),
(45, 3, 55),
(46, 3, 56),
(47, 3, 57),
(48, 3, 58),
(49, 2, 59),
(50, 1, 60);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_preguntasseguridad`
--

CREATE TABLE `tb_preguntasseguridad` (
  `codPregunta` int(11) NOT NULL,
  `pregunta` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tb_preguntasseguridad`
--

INSERT INTO `tb_preguntasseguridad` (`codPregunta`, `pregunta`) VALUES
(1, '¿Nombre de su primera mascota?'),
(2, '¿Cual es su color favorito?'),
(3, '¿Cual es el nombre de su Padre?'),
(4, '¿Cual es su comida favorita?'),
(5, '¿Cual es su pelicula favorita?');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_profesion`
--

CREATE TABLE `tb_profesion` (
  `codProfesion` int(11) NOT NULL,
  `nombreProfesion` varchar(100) NOT NULL,
  `codRubro` int(11) NOT NULL,
  `codEstado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tb_profesion`
--

INSERT INTO `tb_profesion` (`codProfesion`, `nombreProfesion`, `codRubro`, `codEstado`) VALUES
(1, 'Informatica', 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_provincia`
--

CREATE TABLE `tb_provincia` (
  `codProvincia` int(11) NOT NULL,
  `nombreProvincia` varchar(100) NOT NULL,
  `codRegion` int(11) NOT NULL,
  `codEstado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tb_provincia`
--

INSERT INTO `tb_provincia` (`codProvincia`, `nombreProvincia`, `codRegion`, `codEstado`) VALUES
(7, 'Cauquenes', 4, 1),
(15, 'Choapa', 0, 1),
(19, 'Iquique', 0, 1),
(25, 'Capitán Prat', 64, 1),
(26, 'Biobío', 65, 1),
(27, '083', 67, 1),
(28, '102', 68, 1),
(29, '152', 69, 1),
(30, '043', 70, 1),
(31, '021', 71, 1),
(32, '032', 72, 1),
(33, '092', 73, 1),
(34, '072', 74, 1),
(35, '151', 69, 1),
(36, '113', 75, 1),
(37, '011', 76, 1),
(38, '031', 72, 1),
(39, '042', 70, 1),
(40, '061', 77, 1),
(41, '057', 78, 1),
(42, '062', 77, 1),
(43, 'Tamarugal', 16, 1),
(44, 'El Loa', 57, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_region`
--

CREATE TABLE `tb_region` (
  `codRegion` int(11) NOT NULL,
  `nombreRegion` varchar(100) NOT NULL,
  `codEstado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tb_region`
--

INSERT INTO `tb_region` (`codRegion`, `nombreRegion`, `codEstado`) VALUES
(1, 'BioBio', 1),
(2, 'Metropolitana', 1),
(4, 'Del Maule', 1),
(12, 'Coquimbo', 1),
(16, 'Tarapaca', 1),
(57, 'Antofagasta', 1),
(58, 'Ñuble', 1),
(61, 'aaaaaa', 0),
(62, 'Arica y parinacota', 1),
(64, 'Aysén del Gral. Carlos Ibáñez del Campo', 1),
(65, 'Del Biobío', 1),
(66, 'Del+Biobío', 1),
(67, '08', 1),
(68, '10', 1),
(69, '15', 1),
(70, '04', 1),
(71, '02', 1),
(72, '03', 1),
(73, '09', 1),
(74, '07', 1),
(75, '11', 1),
(76, '01', 1),
(77, '06', 1),
(78, '05', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_reporte`
--

CREATE TABLE `tb_reporte` (
  `codReporte` int(11) NOT NULL,
  `runEspecialista` varchar(10) CHARACTER SET utf8mb4 NOT NULL,
  `runCliente` varchar(10) CHARACTER SET utf8mb4 NOT NULL,
  `motivo` varchar(300) NOT NULL,
  `prueba` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_resena`
--

CREATE TABLE `tb_resena` (
  `codResena` int(11) NOT NULL,
  `runCliente` varchar(10) CHARACTER SET utf8mb4 NOT NULL,
  `runEspecialista` varchar(10) CHARACTER SET utf8mb4 NOT NULL,
  `resena` varchar(1000) NOT NULL,
  `calificacion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_respuestaseguridad`
--

CREATE TABLE `tb_respuestaseguridad` (
  `codRespuesta` int(11) NOT NULL,
  `respuesta` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tb_respuestaseguridad`
--

INSERT INTO `tb_respuestaseguridad` (`codRespuesta`, `respuesta`) VALUES
(1, ''),
(2, ''),
(3, ''),
(4, ''),
(5, ''),
(6, ''),
(7, ''),
(8, ''),
(14, 'Asado'),
(15, 'Asado'),
(16, 'Asado'),
(17, 'Asado'),
(18, 'Asado'),
(19, 'Asado'),
(20, 'Asado'),
(21, 'Asado'),
(22, 'Asado'),
(23, 'Asado'),
(24, 'Asado'),
(25, 'Rojo'),
(26, 'Rojo'),
(27, 'Rojo'),
(28, 'Andres'),
(29, 'Andres'),
(30, 'Guillermo'),
(31, 'Gonzalo'),
(32, 'Alex'),
(33, 'Alex'),
(34, 'Alex'),
(35, 'Alex'),
(36, 'Alex'),
(37, 'Alex'),
(38, 'Alex'),
(39, 'Alex'),
(40, 'Alex'),
(41, 'Star Wars'),
(42, 'Star Wars'),
(43, 'Star Wars'),
(44, 'Star Wars'),
(45, 'Star Wars'),
(46, 'Naranjo'),
(47, 'Rojo'),
(48, 'Torta'),
(49, 'Señor de los anillos'),
(50, 'Negro'),
(51, 'Morado'),
(52, 'Faustino'),
(53, 'Rosado'),
(54, 'Rosado'),
(55, 'Angel'),
(56, 'Angel'),
(57, 'Angel'),
(58, 'Angel'),
(59, 'Morado'),
(60, 'Selena');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_rubro`
--

CREATE TABLE `tb_rubro` (
  `codRubro` int(11) NOT NULL,
  `nombreRubro` varchar(200) NOT NULL,
  `codEstado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tb_rubro`
--

INSERT INTO `tb_rubro` (`codRubro`, `nombreRubro`, `codEstado`) VALUES
(1, 'Informática', 1),
(2, 'Electricidad', 1),
(6, 'Construccion', 1),
(7, 'Salud', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_trabajadormes`
--

CREATE TABLE `tb_trabajadormes` (
  `codTrabajadorMes` int(11) NOT NULL,
  `runEspecialista` varchar(10) CHARACTER SET utf8mb4 NOT NULL,
  `fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_trabajo`
--

CREATE TABLE `tb_trabajo` (
  `codTrabajo` int(11) NOT NULL,
  `codOrdenServicio` int(11) NOT NULL,
  `codEstadoTrabajo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `tb_trabajo`
--

INSERT INTO `tb_trabajo` (`codTrabajo`, `codOrdenServicio`, `codEstadoTrabajo`) VALUES
(4, 4, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tb_trabajosespecialista`
--

CREATE TABLE `tb_trabajosespecialista` (
  `codTrabajoEspecialista` int(11) NOT NULL,
  `nombreTrabajo` varchar(100) NOT NULL,
  `valorTrabajo` int(12) NOT NULL,
  `descripcionTrabajo` varchar(400) NOT NULL,
  `codFotosTrabajos` int(11) NOT NULL,
  `codEstado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `tb_trabajosespecialista`
--

INSERT INTO `tb_trabajosespecialista` (`codTrabajoEspecialista`, `nombreTrabajo`, `valorTrabajo`, `descripcionTrabajo`, `codFotosTrabajos`, `codEstado`) VALUES
(1, 'Ensamble equipos', 50000, 'Se ensamblan equipos', 1, 1),
(2, 'Configuracion de equipos', 10000, 'Se configuran equipos con programas necesarios', 1, 1),
(3, 'Formateo equipos', 20000, 'Se formatean equipos, se ofrece copia de seguridad', 1, 1);

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vw_historial_clientes`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vw_historial_clientes` (
`run` varchar(13)
,`estado` varchar(20)
,`NombreCliente` varchar(200)
,`NombreEspecialista` varchar(200)
,`fechaInicio` varchar(10)
,`fechaFin` varchar(10)
,`descripcion` varchar(500)
,`nombreServicio` varchar(60)
);

-- --------------------------------------------------------

--
-- Estructura Stand-in para la vista `vw_perfilespecialista`
-- (Véase abajo para la vista actual)
--
CREATE TABLE `vw_perfilespecialista` (
`nombres` varchar(100)
,`apellidos` varchar(100)
,`telefono` varchar(9)
,`correo` varchar(60)
,`nombreProfesion` varchar(100)
);

-- --------------------------------------------------------

--
-- Estructura para la vista `vw_historial_clientes`
--
DROP TABLE IF EXISTS `vw_historial_clientes`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_historial_clientes`  AS SELECT `cli`.`run` AS `run`, `est`.`estado` AS `estado`, concat(`cli`.`nombres`,'',`cli`.`apellidos`) AS `NombreCliente`, concat(`esp`.`nombres`,'',`esp`.`apellidos`) AS `NombreEspecialista`, date_format(`ord`.`fechaInicio`,'%d-%m-%Y') AS `fechaInicio`, date_format(`ord`.`fechaFin`,'%d-%m-%Y') AS `fechaFin`, `ord`.`descripcion` AS `descripcion`, `ord`.`nombreServicio` AS `nombreServicio` FROM ((((`tb_trabajo` `trab` join `tb_ordenservicio` `ord` on(`trab`.`codOrdenServicio` = `ord`.`codOrdenServicio`)) join `tb_estadotrabajo` `est` on(`trab`.`codEstadoTrabajo` = `est`.`codEstadoTrabajo`)) join `tb_cliente` `cli` on(`ord`.`runCliente` = `cli`.`run`)) join `tb_especialista` `esp` on(`ord`.`runEspecialista` = `esp`.`run`)) ;

-- --------------------------------------------------------

--
-- Estructura para la vista `vw_perfilespecialista`
--
DROP TABLE IF EXISTS `vw_perfilespecialista`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `vw_perfilespecialista`  AS SELECT `esp`.`nombres` AS `nombres`, `esp`.`apellidos` AS `apellidos`, `esp`.`telefono` AS `telefono`, `esp`.`correo` AS `correo`, `pro`.`nombreProfesion` AS `nombreProfesion` FROM (`tb_especialista` `esp` join `tb_profesion` `pro` on(`esp`.`codProfesion` = `pro`.`codProfesion`)) ;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tb_cliente`
--
ALTER TABLE `tb_cliente`
  ADD PRIMARY KEY (`run`),
  ADD UNIQUE KEY `correo` (`correo`),
  ADD KEY `direccion_cliente` (`codDireccion`),
  ADD KEY `perfilCliente_cliente` (`codPerfilCli`),
  ADD KEY `fk_estadoCliente` (`codEstado`),
  ADD KEY `preguntaRespuesta_cliente` (`codPreguntaRespuesta`);

--
-- Indices de la tabla `tb_comuna`
--
ALTER TABLE `tb_comuna`
  ADD PRIMARY KEY (`codComuna`),
  ADD KEY `provincia_comuna` (`codProvincia`),
  ADD KEY `fk_estadoComuna` (`codEstado`);

--
-- Indices de la tabla `tb_detalleordenservicio`
--
ALTER TABLE `tb_detalleordenservicio`
  ADD PRIMARY KEY (`codDetalleOrden`),
  ADD KEY `detalleOrdenServicio_rubro` (`codRubro`),
  ADD KEY `trabajosEspecialista_detalleOrdenServicio` (`codTrabajoEspecialista`);

--
-- Indices de la tabla `tb_direccion`
--
ALTER TABLE `tb_direccion`
  ADD PRIMARY KEY (`codDireccion`),
  ADD KEY `comuna_direccion` (`codComuna`),
  ADD KEY `fk_estadoDireccion` (`codEstado`);

--
-- Indices de la tabla `tb_especialista`
--
ALTER TABLE `tb_especialista`
  ADD PRIMARY KEY (`run`),
  ADD UNIQUE KEY `correo` (`correo`),
  ADD KEY `direccion_especialista` (`codDireccion`),
  ADD KEY `profesion_especialista` (`codProfesion`),
  ADD KEY `perfilEspecialista_especialista` (`codPerfilEsp`),
  ADD KEY `fk_estadoEspecialista` (`codEstado`);

--
-- Indices de la tabla `tb_estado`
--
ALTER TABLE `tb_estado`
  ADD PRIMARY KEY (`codEstado`);

--
-- Indices de la tabla `tb_estadotrabajo`
--
ALTER TABLE `tb_estadotrabajo`
  ADD PRIMARY KEY (`codEstadoTrabajo`);

--
-- Indices de la tabla `tb_fotostrabajos`
--
ALTER TABLE `tb_fotostrabajos`
  ADD PRIMARY KEY (`codFotosTrabajos`);

--
-- Indices de la tabla `tb_ordenservicio`
--
ALTER TABLE `tb_ordenservicio`
  ADD PRIMARY KEY (`codOrdenServicio`),
  ADD KEY `detalleOrdenServicio_ordenServicio` (`codDetalleOrden`),
  ADD KEY `ordenServicio_direccion` (`codDireccion`),
  ADD KEY `cliente_ordenServicio` (`runCliente`),
  ADD KEY `especialista_ordenServicio` (`runEspecialista`);

--
-- Indices de la tabla `tb_perfilcliente`
--
ALTER TABLE `tb_perfilcliente`
  ADD PRIMARY KEY (`codPerfilCli`);

--
-- Indices de la tabla `tb_perfilespecialista`
--
ALTER TABLE `tb_perfilespecialista`
  ADD PRIMARY KEY (`codPerfilEsp`),
  ADD KEY `trabajosEspecialista_perfilEspecialista` (`codTrabajoEspecialista`);

--
-- Indices de la tabla `tb_preguntarespuesta`
--
ALTER TABLE `tb_preguntarespuesta`
  ADD PRIMARY KEY (`codPreguntaRespuesta`),
  ADD KEY `preguntaRespuesta_respuestaSeguridad` (`codRespuesta`),
  ADD KEY `preguntaRespuesta_preguntaSeguridad` (`codPregunta`);

--
-- Indices de la tabla `tb_preguntasseguridad`
--
ALTER TABLE `tb_preguntasseguridad`
  ADD PRIMARY KEY (`codPregunta`);

--
-- Indices de la tabla `tb_profesion`
--
ALTER TABLE `tb_profesion`
  ADD PRIMARY KEY (`codProfesion`),
  ADD KEY `profesion_rubro` (`codRubro`),
  ADD KEY `fk_estadoProfesion` (`codEstado`);

--
-- Indices de la tabla `tb_provincia`
--
ALTER TABLE `tb_provincia`
  ADD PRIMARY KEY (`codProvincia`),
  ADD KEY `region_provincia` (`codRegion`),
  ADD KEY `fk_estadoProvincia` (`codEstado`);

--
-- Indices de la tabla `tb_region`
--
ALTER TABLE `tb_region`
  ADD PRIMARY KEY (`codRegion`),
  ADD KEY `fk_estadoRegion` (`codEstado`);

--
-- Indices de la tabla `tb_reporte`
--
ALTER TABLE `tb_reporte`
  ADD PRIMARY KEY (`codReporte`),
  ADD KEY `cliente_reporte` (`runCliente`),
  ADD KEY `especialista_reporte` (`runEspecialista`);

--
-- Indices de la tabla `tb_resena`
--
ALTER TABLE `tb_resena`
  ADD PRIMARY KEY (`codResena`),
  ADD KEY `cliente_resena` (`runCliente`),
  ADD KEY `especialista_resena` (`runEspecialista`);

--
-- Indices de la tabla `tb_respuestaseguridad`
--
ALTER TABLE `tb_respuestaseguridad`
  ADD PRIMARY KEY (`codRespuesta`);

--
-- Indices de la tabla `tb_rubro`
--
ALTER TABLE `tb_rubro`
  ADD PRIMARY KEY (`codRubro`),
  ADD KEY `fk_estadoRubro` (`codEstado`);

--
-- Indices de la tabla `tb_trabajadormes`
--
ALTER TABLE `tb_trabajadormes`
  ADD PRIMARY KEY (`codTrabajadorMes`),
  ADD KEY `especialista_trabajadorMes` (`runEspecialista`);

--
-- Indices de la tabla `tb_trabajo`
--
ALTER TABLE `tb_trabajo`
  ADD PRIMARY KEY (`codTrabajo`),
  ADD KEY `estadoTrabajo_trabajo` (`codEstadoTrabajo`),
  ADD KEY `ordenServicio_trabajo` (`codOrdenServicio`);

--
-- Indices de la tabla `tb_trabajosespecialista`
--
ALTER TABLE `tb_trabajosespecialista`
  ADD PRIMARY KEY (`codTrabajoEspecialista`),
  ADD KEY `fotosTrabajos_trabajosEspecialista` (`codFotosTrabajos`),
  ADD KEY `fk_estadoTrabajos` (`codEstado`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tb_comuna`
--
ALTER TABLE `tb_comuna`
  MODIFY `codComuna` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT de la tabla `tb_detalleordenservicio`
--
ALTER TABLE `tb_detalleordenservicio`
  MODIFY `codDetalleOrden` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `tb_direccion`
--
ALTER TABLE `tb_direccion`
  MODIFY `codDireccion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT de la tabla `tb_estado`
--
ALTER TABLE `tb_estado`
  MODIFY `codEstado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `tb_estadotrabajo`
--
ALTER TABLE `tb_estadotrabajo`
  MODIFY `codEstadoTrabajo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tb_fotostrabajos`
--
ALTER TABLE `tb_fotostrabajos`
  MODIFY `codFotosTrabajos` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `tb_ordenservicio`
--
ALTER TABLE `tb_ordenservicio`
  MODIFY `codOrdenServicio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `tb_perfilcliente`
--
ALTER TABLE `tb_perfilcliente`
  MODIFY `codPerfilCli` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- AUTO_INCREMENT de la tabla `tb_perfilespecialista`
--
ALTER TABLE `tb_perfilespecialista`
  MODIFY `codPerfilEsp` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tb_preguntarespuesta`
--
ALTER TABLE `tb_preguntarespuesta`
  MODIFY `codPreguntaRespuesta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT de la tabla `tb_preguntasseguridad`
--
ALTER TABLE `tb_preguntasseguridad`
  MODIFY `codPregunta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `tb_profesion`
--
ALTER TABLE `tb_profesion`
  MODIFY `codProfesion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `tb_provincia`
--
ALTER TABLE `tb_provincia`
  MODIFY `codProvincia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT de la tabla `tb_region`
--
ALTER TABLE `tb_region`
  MODIFY `codRegion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=79;

--
-- AUTO_INCREMENT de la tabla `tb_reporte`
--
ALTER TABLE `tb_reporte`
  MODIFY `codReporte` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tb_resena`
--
ALTER TABLE `tb_resena`
  MODIFY `codResena` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tb_respuestaseguridad`
--
ALTER TABLE `tb_respuestaseguridad`
  MODIFY `codRespuesta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT de la tabla `tb_rubro`
--
ALTER TABLE `tb_rubro`
  MODIFY `codRubro` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `tb_trabajadormes`
--
ALTER TABLE `tb_trabajadormes`
  MODIFY `codTrabajadorMes` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tb_trabajo`
--
ALTER TABLE `tb_trabajo`
  MODIFY `codTrabajo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `tb_trabajosespecialista`
--
ALTER TABLE `tb_trabajosespecialista`
  MODIFY `codTrabajoEspecialista` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `tb_cliente`
--
ALTER TABLE `tb_cliente`
  ADD CONSTRAINT `direccion_cliente` FOREIGN KEY (`codDireccion`) REFERENCES `tb_direccion` (`codDireccion`),
  ADD CONSTRAINT `fk_estadoCliente` FOREIGN KEY (`codEstado`) REFERENCES `tb_estado` (`codEstado`),
  ADD CONSTRAINT `perfilCliente_cliente` FOREIGN KEY (`codPerfilCli`) REFERENCES `tb_perfilcliente` (`codPerfilCli`),
  ADD CONSTRAINT `preguntaRespuesta_cliente` FOREIGN KEY (`codPreguntaRespuesta`) REFERENCES `tb_preguntarespuesta` (`codPreguntaRespuesta`);

--
-- Filtros para la tabla `tb_detalleordenservicio`
--
ALTER TABLE `tb_detalleordenservicio`
  ADD CONSTRAINT `detalleOrdenServicio_rubro` FOREIGN KEY (`codRubro`) REFERENCES `tb_rubro` (`codRubro`),
  ADD CONSTRAINT `trabajosEspecialista_detalleOrdenServicio` FOREIGN KEY (`codTrabajoEspecialista`) REFERENCES `tb_trabajosespecialista` (`codTrabajoEspecialista`);

--
-- Filtros para la tabla `tb_direccion`
--
ALTER TABLE `tb_direccion`
  ADD CONSTRAINT `fk_estadoDireccion` FOREIGN KEY (`codEstado`) REFERENCES `tb_estado` (`codEstado`);

--
-- Filtros para la tabla `tb_especialista`
--
ALTER TABLE `tb_especialista`
  ADD CONSTRAINT `direccion_especialista` FOREIGN KEY (`codDireccion`) REFERENCES `tb_direccion` (`codDireccion`),
  ADD CONSTRAINT `fk_estadoEspecialista` FOREIGN KEY (`codEstado`) REFERENCES `tb_estado` (`codEstado`),
  ADD CONSTRAINT `perfilEspecialista_especialista` FOREIGN KEY (`codPerfilEsp`) REFERENCES `tb_perfilespecialista` (`codPerfilEsp`),
  ADD CONSTRAINT `profesion_especialista` FOREIGN KEY (`codProfesion`) REFERENCES `tb_profesion` (`codProfesion`);

--
-- Filtros para la tabla `tb_ordenservicio`
--
ALTER TABLE `tb_ordenservicio`
  ADD CONSTRAINT `cliente_ordenServicio` FOREIGN KEY (`runCliente`) REFERENCES `tb_cliente` (`run`),
  ADD CONSTRAINT `detalleOrdenServicio_ordenServicio` FOREIGN KEY (`codDetalleOrden`) REFERENCES `tb_detalleordenservicio` (`codDetalleOrden`),
  ADD CONSTRAINT `especialista_ordenServicio` FOREIGN KEY (`runEspecialista`) REFERENCES `tb_especialista` (`run`),
  ADD CONSTRAINT `ordenServicio_direccion` FOREIGN KEY (`codDireccion`) REFERENCES `tb_direccion` (`codDireccion`);

--
-- Filtros para la tabla `tb_perfilespecialista`
--
ALTER TABLE `tb_perfilespecialista`
  ADD CONSTRAINT `trabajosEspecialista_perfilEspecialista` FOREIGN KEY (`codTrabajoEspecialista`) REFERENCES `tb_trabajosespecialista` (`codTrabajoEspecialista`);

--
-- Filtros para la tabla `tb_preguntarespuesta`
--
ALTER TABLE `tb_preguntarespuesta`
  ADD CONSTRAINT `preguntaRespuesta_preguntaSeguridad` FOREIGN KEY (`codPregunta`) REFERENCES `tb_preguntasseguridad` (`codPregunta`),
  ADD CONSTRAINT `preguntaRespuesta_respuestaSeguridad` FOREIGN KEY (`codRespuesta`) REFERENCES `tb_respuestaseguridad` (`codRespuesta`);

--
-- Filtros para la tabla `tb_profesion`
--
ALTER TABLE `tb_profesion`
  ADD CONSTRAINT `fk_estadoProfesion` FOREIGN KEY (`codEstado`) REFERENCES `tb_estado` (`codEstado`),
  ADD CONSTRAINT `profesion_rubro` FOREIGN KEY (`codRubro`) REFERENCES `tb_rubro` (`codRubro`);

--
-- Filtros para la tabla `tb_reporte`
--
ALTER TABLE `tb_reporte`
  ADD CONSTRAINT `cliente_reporte` FOREIGN KEY (`runCliente`) REFERENCES `tb_cliente` (`run`),
  ADD CONSTRAINT `especialista_reporte` FOREIGN KEY (`runEspecialista`) REFERENCES `tb_especialista` (`run`);

--
-- Filtros para la tabla `tb_resena`
--
ALTER TABLE `tb_resena`
  ADD CONSTRAINT `cliente_resena` FOREIGN KEY (`runCliente`) REFERENCES `tb_cliente` (`run`),
  ADD CONSTRAINT `especialista_resena` FOREIGN KEY (`runEspecialista`) REFERENCES `tb_especialista` (`run`);

--
-- Filtros para la tabla `tb_rubro`
--
ALTER TABLE `tb_rubro`
  ADD CONSTRAINT `fk_estadoRubro` FOREIGN KEY (`codEstado`) REFERENCES `tb_estado` (`codEstado`);

--
-- Filtros para la tabla `tb_trabajadormes`
--
ALTER TABLE `tb_trabajadormes`
  ADD CONSTRAINT `especialista_trabajadorMes` FOREIGN KEY (`runEspecialista`) REFERENCES `tb_especialista` (`run`);

--
-- Filtros para la tabla `tb_trabajo`
--
ALTER TABLE `tb_trabajo`
  ADD CONSTRAINT `estadoTrabajo_trabajo` FOREIGN KEY (`codEstadoTrabajo`) REFERENCES `tb_estadotrabajo` (`codEstadoTrabajo`),
  ADD CONSTRAINT `ordenServicio_trabajo` FOREIGN KEY (`codOrdenServicio`) REFERENCES `tb_ordenservicio` (`codOrdenServicio`);

--
-- Filtros para la tabla `tb_trabajosespecialista`
--
ALTER TABLE `tb_trabajosespecialista`
  ADD CONSTRAINT `fk_estadoTrabajos` FOREIGN KEY (`codEstado`) REFERENCES `tb_estado` (`codEstado`),
  ADD CONSTRAINT `fotosTrabajos_trabajosEspecialista` FOREIGN KEY (`codFotosTrabajos`) REFERENCES `tb_fotostrabajos` (`codFotosTrabajos`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
