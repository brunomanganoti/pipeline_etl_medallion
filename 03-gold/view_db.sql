SELECT 
    users.id,
    users.nome,
    users.email,
    users.telefone,
    users.cep,
    users.data_nascimento,
    users.genero,
    info_cep.localidade,
    info_cep.uf,
    info_cep.logradouro,
    info_cep.bairro,
    info_cep.regiao,
    info_cep.ibge,
    info_cep.gia,
    info_cep.ddd,
    info_cep.siafi
FROM users
JOIN info_cep ON
users.cep = info_cep.cep
ORDER BY CAST(users.id AS INT);