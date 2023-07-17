<?php
require_once 'funcoes_crud.php'; // Importar o arquivo com as funções de CRUD

// Obter os valores enviados pelo formulário
$nome_aluno = $_POST['nome'];
$telefone_aluno = $_POST['telefone'];
$email_aluno = $_POST['email'];
$sexo_aluno = $_POST['sexo'];

function criar_aluno($nome, $telefone, $email, $sexo) {
    // Chamar a função Python criar_alunos() com os valores
    exec("python3 funcoes_crud.py criar_alunos " . escapeshellarg($nome) . " " . escapeshellarg($telefone) . " " . escapeshellarg($email) . " " . escapeshellarg($sexo));

    echo "Aluno criado com sucesso!";
}