CREATE VIEW vw_pesagem_detalhada AS
SELECT 
    v.id AS veiculo_id,
    v.placa,
    v.modelo,
    v.tipo,
    p.id AS pesagem_id,
    p.peso_bruto,
    p.peso_tara,
    p.peso_liquido,
    p.data_pesagem
FROM 
    veiculos v
INNER JOIN 
    pesagens p ON v.id = p.veiculo_id;