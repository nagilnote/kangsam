        if vulnerable_topics:
            doc.add_paragraph('다음 문항들에서 높은 오답률이 관찰되었습니다. 학습자들이 겪고 있는 혼란을 바로잡기 위한 개념 재검토가 필요합니다.')
            for num, topic, rate in vulnerable_topics:
                doc.add_paragraph(f'■ 문항 {num} (정답 추정률 {rate:.1f}% - 개선 필요)')
                doc.add_paragraph(f'  - 관련 내용: {topic}')
                doc.add_paragraph('  - 제안: 가장 많이 선택된 오답 보기와 정답의 차이를 명확히 비교 설명하고, 실무 현장에서 이 개념이 어떻게 적용되는지 예시를 들어 보충해 주십시오.')
        else:
            doc.add_paragraph('전반적인 이해도가 우수합니다. 현재의 교육 방향을 유지하셔도 좋습니다.')
            
        # 6. 파일 다운로드 준비
        doc_stream = io.BytesIO()
        doc.save(doc_stream)
        doc_stream.seek(0)
        
        st.success("분석 보고서가 완성되었습니다! 아래 버튼을 눌러 다운로드하세요.")
        
        st.download_button(
            label="📥 분석 결과 문서 다운로드 (.docx)",
            data=doc_stream,
            file_name="요양보호_성취도_분석결과.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
        
    except Exception as e:
        st.error(f"데이터를 처리하는 중 오류가 발생했습니다: {str(e)}")
