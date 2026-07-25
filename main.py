#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def search_legal_documents(query: str, documents: list[str]) -> list[tuple[str, int]]:
    """
    Simulates an AI-powered search for legal documents based on keywords.
    It returns documents ranked by a simple relevance score (number of matching keywords).
    """
    query_keywords = set(re.findall(r'\b\w+\b', query.lower()))
    results = []

    # Simulate processing a corpus of legal texts
    for i, doc in enumerate(documents):
        doc_lower = doc.lower()
        score = 0
        matched_keywords = []
        for keyword in query_keywords:
            if keyword in doc_lower:
                score += 1
                matched_keywords.append(keyword)
        
        if score > 0:
            # This part illustrates the core concept: AI helping find relevant info.
            # In a real OpenThai 2.0 Legal model, this would involve complex NLP,
            # semantic search, and legal reasoning, not just keyword matching.
            results.append((doc, score, matched_keywords))

    # Sort results by relevance score in descending order
    results.sort(key=lambda x: x[1], reverse=True)
    return results


if __name__ == "__main__":
    # Simulate a corpus of legal documents. Some contain placeholder Thai characters
    # to represent the 'Thai Law' context and language barrier mentioned in the article.
    legal_corpus = [
        "Madde 123: Bu yasa, Tayland Krallığı'nda kişisel verilerin korunmasını düzenler. ข้อมูลส่วนบุคคล (Personal Data) is defined as sensitive information.",
        "Karar No. 456: Mahkeme, fikri mülkiyet hakları (Intellectual Property Rights) ile ilgili bir davayı inceledi. สิทธิในทรัพย์สินทางปัญญา protects creative works.",
        "Yönetmelik 789: Çevre koruma (Environmental Protection) standartları ve sürdürülebilirlik ilkeleri. การคุ้มครองสิ่งแวดล้อม is crucial for future generations.",
        "Madde 101: Ticaret hukuku (Commercial Law) ve sözleşmelerin geçerliliği. กฎหมายการค้า governs business transactions.",
        "Dava Özeti: Kişisel verilerin izinsiz kullanımı ve gizlilik ihlali. Hukuki atıflar ve emsal kararlar incelendi.",
        "Yasa Taslağı: Yeni fikri mülkiyet düzenlemeleri ve teknolojik gelişmelerin etkisi. Patent ve telif hakları."
    ]

    # Example Turkish query, simulating a lawyer's search for information.
    # The article highlights how AI can simplify complex legal research.
    turkish_query = "kişisel veri koruma ve gizlilik"
    print(f"Aranan terim: '{turkish_query}'\n")

    found_documents = search_legal_documents(turkish_query, legal_corpus)

    if found_documents:
        print("Bulunan ilgili belgeler:")
        for doc, score, matched_keywords in found_documents:
            print(f"---\nRelevance Score: {score} (Matched: {', '.join(matched_keywords)})\n{doc}\n---")
    else:
        print("İlgili belge bulunamadı.")

    print("\n--- İkinci Sorgu ---")
    turkish_query_2 = "fikri mülkiyet hakları"
    print(f"Aranan terim: '{turkish_query_2}'\n")
    found_documents_2 = search_legal_documents(turkish_query_2, legal_corpus)
    if found_documents_2:
        print("Bulunan ilgili belgeler:")
        for doc, score, matched_keywords in found_documents_2:
            print(f"---\nRelevance Score: {score} (Matched: {', '.join(matched_keywords)})\n{doc}\n---")
    else:
        print("İlgili belge bulunamadı.")