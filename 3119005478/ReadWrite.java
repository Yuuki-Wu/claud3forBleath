public class ReadWrite {
	public static void main(String[] args) throws IOException {
		Path path1 = Paths.get("D:/origin.txt");
		Path path2 = Paths.get("D:/Plagiarism.txt");//读取文件	
		File file = new File("D:/answer.txt");//写入文件
		FileWriter fileWriter = new FileWriter(file);
		byte[] data;
		try {
			data = Files.readAllBytes(path1);
			String s1= new String(data, "utf-8");
			data = Files.readAllBytes(path2);
			String s2=new String(data, "utf-8");
			SimilarityCheck t2 =new SimilarityCheck(s1,s2);	
			double sim = t2.sim();
		    System.out.println("相似度为"+String.format("%.2f", sim));//保留小数点后两位
		    fileWriter.write("相似度为"+String.format("%.2f", sim));
		    fileWriter.close();

		} catch (Exception e) {
			System.out.println("读取文件内容操作出错");
			fileWriter.write("读取文件内容操作出错");
		    fileWriter.close();
			e.printStackTrace();
		}			
	}}
